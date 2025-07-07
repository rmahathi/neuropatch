# Components List – NEUROPATCH System

A bill of materials (BOM) for the cognitive attention & workload monitoring patch using Raspberry Pi Pico W.

| # | Component              | Part Number / Type          | Qty | Estimated Cost (INR) | Purpose / Notes                                       |
|---|------------------------|-----------------------------|-----|-----------------------|--------------------------------------------------------|
| 1 | Raspberry Pi Pico W    | RP2040 microcontroller      | 1   | ₹500 – ₹650           | Main controller with Wi-Fi, ADC, I2C                   |
| 2 | MAX30102 Module        | HR/SpO₂ Sensor              | 1   | ₹300 – ₹350           | PPG sensor for HR, HRV analysis                        |
| 3 | GSR Sensor Module v2   | Analog skin conductance     | 1   | ₹1,500 – ₹1,600       | Measures skin resistance (EDA, stress)                 |
| 4 | OLED Display (0.96”)   | SSD1306, I2C, 128x64        | 1   | ₹160 – ₹220           | Real-time visualization of focus, HRV, GSR             |
| 5 | LED (3mm or 5mm)       | Any color                   | 1   | ₹5 – ₹10              | Visual feedback for attention drop                     |
| 6 | Resistor – 220Ω        | Through-hole or SMD         | 1   | ₹2 – ₹5               | Current limiter for LED                                |
| 7 | Pull-up Resistors      | 4.7kΩ, 1/4W                 | 2   | ₹2 × 2 = ₹4           | For I2C SDA/SCL pull-up                                |
| 8 | Jumper Wires (F–F)     | Dupont 10–15 cm             | 10  | ₹30 – ₹50             | Easy breadboard sensor wiring                          |
| 9 | Breadboard             | 400 or 830 point (optional) | 1   | ₹80 – ₹120            | For temporary connections                              |
|10 | Micro-USB Cable        | USB-A to Micro-USB          | 1   | ₹60 – ₹100            | For power + data logging                               |

**Total Estimated Cost:** ₹2,700 – ₹3,200 (well under ₹8,000 cap)

## Notes
- All sensors operate at **3.3V logic**, directly compatible with Pico W.
- No separate power module is required — USB powers the entire system.