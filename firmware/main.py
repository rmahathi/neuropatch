from machine import Pin, I2C, ADC
from time import sleep
from max30102 import MAX30102

# Setup I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Initialize sensor
sensor = MAX30102()
sensor.init(i2c)  # Proper initialization using your init()
# sensor.setup_sensor() <-- Already called within init()

# Setup GSR ADC
gsr_adc = ADC(26)

# GSR Threshold
GSR_THRESHOLD = 30000

while True:
    try:
        red_buf, ir_buf = sensor.read_sequential()
        red = red_buf[0] if red_buf else 0
        ir = ir_buf[0] if ir_buf else 0

        gsr_val = gsr_adc.read_u16()
        focus = "Low" if gsr_val > GSR_THRESHOLD else "OK"

        print("Red: {}, IR: {}, GSR: {}, Focus: {}".format(red, ir, gsr_val, focus))
    except Exception as e:
        print("Sensor read error:", e)

    sleep(0.5)
