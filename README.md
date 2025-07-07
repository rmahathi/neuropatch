# Neuropatch - A Physiological Signal-Based Patch for Cognitive Load and Attention Assessment in ADHD

## Summary
India faces persistent challenges in delivering affordable and scalable health monitoring, especially in rural areas. The high cost and import dependency of medical devices, such as cardiac and neonatal monitors, limit access to vital care.

Praan addresses this gap by developing a RISC-V-based open-source System-on-Chip (SoC) platform, optimized for vital health monitoring in hospitals and structured home care. Built around the Shakti Yamuna core from IIT Madras, the system integrates medical signal processing accelerators, sensor interfaces, and efficient power management, enabling real-time processing of ECG, PPG, and temperature data.

The platform will first be validated on FPGA and later developed as an ASIC with support from MIETY/BIRAC. Praan aims to reduce the bill of materials (BOM) by 20–30%, accelerate product development for startups and MSMEs, and strengthen India’s self-reliance in MedTech under Atmanirbhar Bharat and the National Digital Health Mission.

Ultimately, Praan empowers India’s healthcare ecosystem with a customizable, certifiable, and cost-effective solution to expand life-saving monitoring across PHCs, hospitals, and home care environments.

## Sensors Used
MAX30102 – PPG (Photoplethysmography) Sensor

- Type: Optical pulse sensor
Purpose: Measures heart rate, heart rate variability (HRV), and blood oxygen (SpO₂) using light absorption.
Interface: I²C
Power: 3.3V
Pin Mapping: SDA → GP0, SCL → GP1

- GSR Sensor Module v2 – Galvanic Skin Response Sensor
Type: Analog electrodermal activity (EDA) sensor
Purpose: Measures skin conductance/resistance, which correlates with cognitive load, stress, or attention.
Interface: Analog voltage output
Power: 3.3V
Pin Mapping: OUT → GP26 (ADC0)

- Sensor Display:
SSD1306 OLED Display (128x64)
Type: I²C graphical display
Purpose: Used to visualize HR, HRV, GSR, and cognitive state in real time
Interface: I²C (shared with MAX30102)
Pin Mapping: SDA → GP0, SCL → GP1
