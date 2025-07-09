import network
import time
import os
from machine import Pin, I2C, ADC
from max30102 import MAX30102

# -------- Circular Buffer Class --------
class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
        self.index = 0

    def add(self, value):
        self.buffer[self.index] = value
        self.index = (self.index + 1) % self.size

    def get(self):
        return self.buffer

    def is_full(self):
        return all(v != 0 for v in self.buffer)

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

# ---- Timestamp Format ----
def get_timestamp():
    t = time.localtime()
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*t[:6])

# ---- Sensor Setup ----
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
ppg = MAX30102()
ppg.init(i2c)
gsr = ADC(Pin(26))

# ---- Data Buffers ----
ir_buf = CircularBuffer(100)
red_buf = CircularBuffer(100)

# ---- Connect to Wi-Fi ----
connect_wifi('Poorvi306', '9449254137')

# ---- Create CSV Log File ----
log_name = "log_" + get_timestamp().replace(":", "-").replace(" ", "_") + ".csv"
with open(log_name, "w") as f:
    f.write("Timestamp,GSR_Voltage,IR,RED\n")

start_time = time.ticks_ms()

# ---- Main Logging Loop ----
while True:
    # Stop after 10 minutes
    if time.ticks_diff(time.ticks_ms(), start_time) > 600000:
        print("10 minutes completed. Logging stopped.")
        break

    try:
        # Read PPG data
        red_samples, ir_samples = ppg.read_sequential(1)
        red = red_samples[0]
        ir = ir_samples[0]

        # Store to buffers
        red_buf.add(red)
        ir_buf.add(ir)

        # GSR voltage
        gsr_val = gsr.read_u16()
        gsr_volt = (gsr_val / 65535.0) * 3.3

        # Log and print
        timestamp = get_timestamp()
        line = "{},{:.2f},{},{}\n".format(timestamp, gsr_volt, ir, red)
        print(line.strip())

        with open(log_name, "a") as f:
            f.write(line)

    except Exception as e:
        print("Error:", e)

    time.sleep(0.5)