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

NEUROPATCH aims to achieve TRL‑8 (Technology Readiness Level 8), signifying that the prototype is tested, validated, and ready for deployment in real-world environments.

---
### Requirements freeze / CTQ table completed
---
---
### Bench accuracy & linearity tested (± specified % FS)
---
---
### 12–24 h continuous data log captured with timestamps
---
---
### Temperature drift evaluated over available range
---
---
### Noise & warm‑up drift quantified
---
---
### 100 h basic endurance run (or summary of longer run)
---
---
### Field simulation ≥ 24 h in intended environment
---
---
### System uptime ≥ 98 % during field test
---
---
### All documentation uploaded: code, BOM, graphs, risk log
---
---
### Sensor‑swap readiness statement included
---
## Setup Steps



