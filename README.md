# Neuropatch - A Physiological Signal-Based Patch for Cognitive Load and Attention Assessment in ADHD

## Summary
**NEUROPATCH** is a wearable physiological monitoring patch designed by Team VitalCore (Aishwarya Joshi and Mahathi R.) for the ELCIA Sensor Hackathon 2025. It enables real-time assessment of **cognitive load**, **attention**, and **stress**, particularly for individuals with ADHD. The device leverages two key biosensors: the **MAX30102 PPG sensor** for heart rate and heart rate variability (HRV), and a **GSR sensor** for electrodermal activity. These signals reflect autonomic nervous system activity and help quantify mental states such as focus, arousal, and fatigue. Built on the **Raspberry Pi Pico W**, the patch supports BLE communication, onboard signal processing, and data logging. The system emphasizes low cost, modularity, and TRL-8 readiness through rigorous sensor testing and characterization. 

NEUROPATCH aims to bridge the gap between clinical-grade cognitive monitoring and accessible, portable solutions for schools, mental health screenings, and personal neurofeedback.

## Sensors Used
| Sensor             | Type          | Purpose                       | Interface | Power | Pins                 |
|--------------------|---------------|-------------------------------|-----------|-------|----------------------|
| **MAX30102**       | Optical (PPG) | HR, HRV, SpO₂ monitoring      | I²C       | 3.3V  | SDA → GP0, SCL → GP1 |
| **GSR Sensor v2**  | Analog (EDA)  | Stress / attention monitoring | Analog    | 3.3V  | OUT → GP26 (ADC0)    |

## 🛠 Setup Steps: Getting Started with NeuroPatch

Follow these steps to set up your development environment for the *NeuroPatch* project on the Raspberry Pi Pico W using *MicroPython* and *Thonny IDE*.

### 1. Install Required Software

#### Thonny IDE
Thonny is a beginner-friendly Python IDE that supports MicroPython out of the box.

- Download from: [https://thonny.org](https://thonny.org)
- Install for your OS (Windows/macOS/Linux)

#### Drivers (if needed)
For Windows: If Pico W is not detected as a USB device, install the USB serial driver:
- [Download](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

### 2️. Flash MicroPython onto the Pico W

Your Pico W must be flashed with MicroPython firmware before programming.

#### Steps:

1. **Hold down the BOOTSEL button** on your Pico W  
2. Plug the Pico W into your computer via USB  
3. It will mount as a storage device called RPI-RP2  
4. Download the latest firmware .uf2 file for Pico W from:  
   👉 [https://micropython.org/download/rp2-pico-w/](https://micropython.org/download/rp2-pico-w/)
   > Recommended: v1.25.0 or latest stable release

5. Drag and drop the .uf2 file into the RPI-RP2 drive  
6. The board will reboot and disappear from File Explorer — MicroPython is now installed 🎉

### 3. Set Up Thonny to Work with Pico W

1. Open *Thonny*
2. Go to *Tools → Options → Interpreter*
3. Under *Interpreter*, select:
   - *MicroPython (Raspberry Pi Pico)*
   - Port: Choose the one that says "USB Serial" (if unsure, select auto connect)
4. Click *OK*
5. In the bottom right, you should now see:  
   MicroPython (Raspberry Pi Pico)

### 4. Upload Project Files to Pico W

1. In Thonny, go to *View → Files* to open the file manager
2. On the *left, browse your PC; on the **right*, your Pico W's file system
3. Upload the following files to the Pico:

| File Name           | Description                       |
|---------------------|-----------------------------------|
| main.py           | Main application logic              |
| max30102.py       | Driver for MAX30102 sensor          |
| circularbuffer.py | Buffer + math utilities for signals |

To upload:
- Right-click file → *Upload to /*

### 5. Run the Code

- Click the green *Run* ▶ button in Thonny
- Your Pico W will start collecting:
  - GSR voltage from ADC
  - IR/RED light data from MAX30102
  - Compute SpO₂ and Heart Rate
  - Log everything to a .csv file on the device

## TRL-8 Goals (PLACEHOLDER!!!)
NEUROPATCH is designed to meet TRL‑8 readiness, demonstrating reliability, stability, and real-world deployability. The following characterization steps are planned:

1. **Requirements Freeze & CTQ Table**
   - Define Critical-to-Quality parameters for MAX30102 and GSR sensors including accuracy, drift, and range.

2. **Bench Accuracy & Linearity Testing**
   - Compare measured values with standard references (e.g., Polar H10 for HRV, synthetic GSR resistors).

3. **1-Hour Continuous Logging**
   - Perform extended runs and export timestamped .csv logs for Origin/Excel-based analysis.

4. **Temperature Drift Evaluation** 
   - Evaluate signal variation across a range of ambient temperatures using controlled airflow.

5. **Noise & Warm-Up Drift**
   - Record output during the first 10 minutes after startup to assess baseline shift and sensor stabilization.

6. **Motion Artifact Simulation**
   - Induce motion while recording to observe signal degradation and filtering effectiveness.

7. **Repeatability Testing**
   - Repeat identical tasks across multiple days to evaluate signal stability and response consistency.

9. **Sensor Swap Readiness**
   - Prototype alternatives using Indian components (e.g., LM358-based GSR circuit, ProtoCentral PPG module).

10. **Documentation & Visuals**
    - Upload all circuit diagrams, firmware, test plots, BOM, and logs to /hardware, /firmware, and /test_logs as per repo structure.




