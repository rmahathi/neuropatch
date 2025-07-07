# Neuropatch - A Physiological Signal-Based Patch for Cognitive Load and Attention Assessment in ADHD

## Summary
**NEUROPATCH** is a wearable physiological monitoring patch designed by Team VitalCore (Aishwarya Joshi and Mahathi R.) for the ELCIA Sensor Hackathon 2025. It enables real-time assessment of **cognitive load**, **attention**, and **stress**, particularly for individuals with ADHD. The device leverages two key biosensors: the **MAX30102 PPG sensor** for heart rate and heart rate variability (HRV), and a **GSR sensor** for electrodermal activity. These signals reflect autonomic nervous system activity and help quantify mental states such as focus, arousal, and fatigue. Built on the **Raspberry Pi Pico W**, the patch supports BLE communication, onboard signal processing, and data logging. The system emphasizes low cost, modularity, and TRL-8 readiness through rigorous sensor testing and characterization. 

NEUROPATCH aims to bridge the gap between clinical-grade cognitive monitoring and accessible, portable solutions for schools, mental health screenings, and personal neurofeedback.

## Sensors Used
| Sensor             | Type          | Purpose                       | Interface | Power | Pins                 |
|--------------------|---------------|-------------------------------|-----------|-------|----------------------|
| **MAX30102**       | Optical (PPG) | HR, HRV, SpO₂ monitoring      | I²C       | 3.3V  | SDA → GP0, SCL → GP1 |
| **GSR Sensor v2**  | Analog (EDA)  | Stress / attention monitoring | Analog    | 3.3V  | OUT → GP26 (ADC0)    |

## TRL-8 Goals

The NEUROPATCH system is designed to meet TRL‑8 standards, indicating that it is ready for real-world deployment with complete validation. The following goals guide its characterization and field readiness:

1. **Requirements Freeze & CTQ Table**  
   Clearly define all Critical-to-Quality metrics (accuracy, range, drift, etc.) for sensors and system.

2. **Bench Accuracy & Linearity Testing**  
   Compare HR and HRV data with reference devices (e.g., Polar H10) and validate GSR linearity over physiological range.

3. **12–24 Hour Continuous Logging**  
   Ensure stable, timestamped data capture for extended durations without data loss.

4. **Temperature Drift Evaluation**  
   Evaluate sensor stability under varying ambient conditions such as heat, cold, and airflow.

5. **Noise & Warm-Up Drift Quantification**  
   Characterize sensor behavior during initial 5–10 minutes after power-on, assessing baseline drift and noise.

6. **100+ Hour Endurance Run**  
   Stress-test the system through prolonged use to confirm hardware durability and consistent signal quality.

7. **24+ Hour Field Simulation**  
   Deploy the patch in realistic scenarios (e.g., study, work sessions) to validate usability and data robustness.

8. **System Uptime ≥ 98%**  
   The device must maintain full functionality with minimal interruptions during all logging sessions.

9. **Full Documentation Submission**  
   Upload code, BOM, circuit diagrams, test data, sensor plots, and risk logs.

10. **Sensor-Swap Readiness**  
    Provide functional alternatives using Indian components (e.g., LM358 GSR circuit, ProtoCentral PPG sensor).


## Setup Steps



