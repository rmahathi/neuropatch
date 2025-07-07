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
The NEUROPATCH system aims to achieve TRL‑8 (Technology Readiness Level 8), signifying that the prototype is tested, validated, and ready for deployment in real-world environments.
---
| No. | Goal                                | Description |
|-----|-------------------------------------|-------------|
| 1️⃣  | Requirements Freeze & CTQ Table     | Define Critical-to-Quality metrics such as accuracy, drift, and sensor range. |
| 2️⃣  | Bench Accuracy & Linearity Testing  | Compare PPG/GSR output with reference devices (e.g., Polar H10) to validate accuracy and signal linearity. |
| 3️⃣  | 12–24 Hour Continuous Logging       | Ensure robust, timestamped data capture with no signal loss over extended sessions. |
| 4️⃣  | Temperature Drift Evaluation        | Test stability of sensor readings under thermal variation (heat, cold, airflow). |
| 5️⃣  | Noise & Warm-Up Drift               | Observe sensor signal behavior during the first 10 minutes after power-up. |
| 6️⃣  | 100+ Hour Endurance Run             | Run device continuously over 4+ days to validate hardware reliability. |
| 7️⃣  | 24+ Hour Field Simulation           | Deploy the patch in a real-life environment and task cycle (e.g., student use). |
| 8️⃣  | System Uptime ≥ 98%                 | Maintain system availability and logging without unexpected crashes or resets. |
| 9️⃣  | Full Documentation Submission       | Include code, BOM, circuit diagrams, sensor logs, analysis, and risk assessment. |
| 🔁  | Sensor-Swap Readiness                | Demonstrate fallback Indian substitutes for sensors (e.g., LM358 GSR, ProtoCentral PPG). |
---

## Setup Steps



