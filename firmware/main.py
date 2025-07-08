import network
import time
import os
from machine import Pin, I2C, ADC
from max30102 import MAX30102

# ---- Wi-Fi Setup ----
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        wlan.connect(ssid, password)
        start = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > 10000:
                print("Wi-Fi connection timed out.")
                return None
            time.sleep(0.5)
    print('Connected. IP:', wlan.ifconfig()[0])
    return wlan

# ---- Time Format Helper ----
def get_timestamp():
    t = time.localtime()
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*t[:6])

# ---- Initialize I2C and Sensor ----
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
sensor = MAX30102()
sensor.init(i2c)

gsr_adc = ADC(26)
GSR_THRESHOLD = 30000

# ---- Connect Wi-Fi ----
connect_wifi('Poorvi306', '9449254137')  # Replace with your Wi-Fi credentials

# ---- Create Unique Log File ----
log_name = "log_" + get_timestamp().replace(":", "-").replace(" ", "_") + ".csv"
with open(log_name, "w") as f:
    f.write("Timestamp,Red,IR,GSR,Focus\n")

# ---- Data Collection Loop ----
while True:
    try:
        red_buf, ir_buf = sensor.read_sequential()
        red = red_buf[0] if red_buf else 0
        ir = ir_buf[0] if ir_buf else 0

        gsr_val = gsr_adc.read_u16()
        focus = "Low" if gsr_val > GSR_THRESHOLD else "OK"

        timestamp = get_timestamp()
        csv_line = "{},{},{},{},{}\n".format(timestamp, red, ir, gsr_val, focus)
        print_line = "{} | red = {}, ir = {}, GSR = {}, focus = {}".format(timestamp, red, ir, gsr_val, focus)

        print(print_line)

        # Append to log file
        with open(log_name, "a") as f:
            f.write(csv_line)

    except Exception as e:
        print("Sensor read error:", e)

    time.sleep(0.5)