from time import sleep_us
from micropython import const
import ustruct

class MAX30102:
    def init(self, i2c, address=0x57):
        self.i2c = i2c
        self.address = address
        self.reset()
        self.setup_sensor()

    def reset(self):
        self.write_reg(0x09, 0x40)
        sleep_us(10000)

    def setup_sensor(self):
        self.write_reg(0x09, 0x03)  # Mode: SpO2
        self.write_reg(0x0A, 0x27)  # SpO2 config
        self.write_reg(0x0C, 0x24)  # LED pulse amp

    def read_sequential(self, num_samples=1):
        red_buf = []
        ir_buf = []
        for _ in range(num_samples):
            try:
                self.write_reg(0x06, 0)
                data = self.read_reg(0x07, 6)
                red = (data[0] << 16 | data[1] << 8 | data[2]) & 0x03FFFF
                ir = (data[3] << 16 | data[4] << 8 | data[5]) & 0x03FFFF
                red_buf.append(red)
                ir_buf.append(ir)
            except:
                red_buf.append(0)
                ir_buf.append(0)
            sleep_us(5000)
        return red_buf, ir_buf

    def write_reg(self, reg, val):
        self.i2c.writeto_mem(self.address, reg, bytes([val]))

    def read_reg(self, reg, num_bytes=1):
        return self.i2c.readfrom_mem(self.address, reg, num_bytes)
