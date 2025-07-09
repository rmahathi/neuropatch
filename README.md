# Neuropatch - A Physiological Signal-Based Patch for Cognitive Load and Attention Assessment in ADHD

## Summary
NEUROPATCH is a compact, wearable physiological monitoring device developed by Team VitalCore (Aishwarya Joshi and Mahathi R.) as part of the ELCIA TRL-8 Sensor Hackathon 2025. It is designed for real-time, non-invasive assessment of cognitive load, attention state, and stress reactivity—particularly in use cases involving neurodivergent populations (e.g., ADHD), as well as in high-focus environments such as classrooms, driver fatigue monitoring, and productivity tracking.

### 1. Integrated Biosensing Modalities
The NEUROPATCH device combines two primary biosensors to extract features reflecting autonomic nervous system activity:

| Sensor             | Type          | Purpose                       | Interface | Power | Pins                 |
|--------------------|---------------|-------------------------------|-----------|-------|----------------------|
| **MAX30102**       | Optical (PPG) | HR, HRV, SpO₂ monitoring      | I²C       | 3.3V  | SDA → GP0, SCL → GP1 |
| **GSR Sensor v2**  | Analog (EDA)  | Stress / attention monitoring | Analog    | 3.3V  | OUT → GP26 (ADC0)    |

### MAX30102 PPG Sensor
A reflective photoplethysmographic (PPG) sensor used to capture volumetric changes in blood flow at the skin surface. From this signal, the device estimates:
   * Heart Rate (HR)
   * Heart Rate Variability (HRV)
These features serve as indicators of parasympathetic tone, which correlates with attentional engagement and cognitive effort.

### GSR (Galvanic Skin Response) Sensor
A skin conductance sensor that measures electrodermal activity via electrodes placed on fingers or palm. GSR tracks sympathetic nervous system arousal, which spikes during stress, anxiety, or high mental workload.

### 2. System Architecture

The sensors interface with a Raspberry Pi Pico W microcontroller that performs the following tasks:

* Acquires real-time biosignals (analog + I²C)
* Performs threshold-based logic to detect attention lapses
* Drives a status LED alert (via GP15)
* Displays HR and GSR values on a 128×64 I²C OLED screen
* Optionally transmits raw data via USB serial for further analysis

### 3. Motivation & Technical Differentiator

NEUROPATCH offers a low-cost, research-oriented alternative to commercial fitness bands. It is designed for modular experimentation and signal-level access, making it suitable for:

* Cognitive attention and stress tracking
* ADHD screening studies
* Embedded health analytics and edge-AI inference
* Academic research on autonomic physiology

Signal fusion of HRV (vagal tone) and EDA (sympathetic arousal) enables a richer interpretation of cognitive state compared to unimodal systems.

## Setup Steps: Getting Started with NeuroPatch

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

## TRL-8 Goals
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




