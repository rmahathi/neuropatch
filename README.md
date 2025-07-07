# Neuropatch - A Physiological Signal-Based Patch for Cognitive Load and Attention Assessment in ADHD

## Summary
**NEUROPATCH** is a wearable physiological monitoring patch designed by Team VitalCore (Aishwarya Joshi and Mahathi R.) for the ELCIA Sensor Hackathon 2025. It enables real-time assessment of **cognitive load**, **attention**, and **stress**, particularly for individuals with ADHD. The device leverages two key biosensors: the **MAX30102 PPG sensor** for heart rate and heart rate variability (HRV), and a **GSR sensor** for electrodermal activity. These signals reflect autonomic nervous system activity and help quantify mental states such as focus, arousal, and fatigue. Built on the **Raspberry Pi Pico W**, the patch supports BLE communication, onboard signal processing, and data logging. The system emphasizes low cost, modularity, and TRL-8 readiness through rigorous sensor testing and characterization. 

NEUROPATCH aims to bridge the gap between clinical-grade cognitive monitoring and accessible, portable solutions for schools, mental health screenings, and personal neurofeedback.

## Sensors Used
| Sensor             | Type          | Purpose                       | Interface | Power | Pins                 |
|--------------------|---------------|-------------------------------|-----------|-------|----------------------|
| **MAX30102**       | Optical (PPG) | HR, HRV, SpO₂ monitoring      | I²C       | 3.3V  | SDA → GP0, SCL → GP1 |
| **GSR Sensor v2**  | Analog (EDA)  | Stress / attention monitoring | Analog    | 3.3V  | OUT → GP26 (ADC0)    |


## TRL-8 Goals (PLACEHOLDER!!!)
NEUROPATCH is designed to meet TRL‑8 readiness, demonstrating reliability, stability, and real-world deployability. The following characterization steps are planned:

1️⃣ **Requirements Freeze & CTQ Table**
   - Define Critical-to-Quality parameters for MAX30102 and GSR sensors including accuracy, drift, and range.

2️⃣ **Bench Accuracy & Linearity Testing**
   - Compare measured values with standard references (e.g., Polar H10 for HRV, synthetic GSR resistors).

3️⃣ **24-Hour Continuous Logging**
   - Perform extended runs and export timestamped .csv logs for Origin/Excel-based analysis.

4️⃣ **Temperature Drift Evaluation** 
   - Evaluate signal variation across a range of ambient temperatures using controlled airflow.

5️⃣ **Noise & Warm-Up Drift**
   - Record output during the first 10 minutes after startup to assess baseline shift and sensor stabilization.

6️⃣ **Motion Artifact Simulation**
   - Induce motion while recording to observe signal degradation and filtering effectiveness.

7️⃣ **Repeatability Testing**
   - Repeat identical tasks across multiple days to evaluate signal stability and response consistency.

8️⃣ **Sensor Swap Readiness**
   - Prototype alternatives using Indian components (e.g., LM358-based GSR circuit, ProtoCentral PPG module).

9️⃣ **Endurance & Field Simulation**
   - Run the system for 100+ hours and perform ≥24h field usage tests in intended settings (e.g., classroom, workstation).

🔟. **Documentation & Visuals**
    - Upload all circuit diagrams, firmware, test plots, BOM, and logs to /hardware, /firmware, and /test_logs as per repo structure.


## Setup Steps



