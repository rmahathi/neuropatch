# Neuropatch - A Physiological Signal-Based Patch for Cognitive Load and Attention Assessment in ADHD

## Summary
**NEUROPATCH** is a wearable physiological monitoring patch designed by Team VitalCore (Aishwarya Joshi and Mahathi R.) for the ELCIA Sensor Hackathon 2025. It enables real-time assessment of **cognitive load**, **attention**, and **stress**, particularly for individuals with ADHD. The device leverages two key biosensors: the **MAX30102 PPG sensor** for heart rate and heart rate variability (HRV), and a **GSR sensor** for electrodermal activity. These signals reflect autonomic nervous system activity and help quantify mental states such as focus, arousal, and fatigue. Built on the **Raspberry Pi Pico W**, the patch supports BLE communication, onboard signal processing, and data logging. The system emphasizes low cost, modularity, and TRL-8 readiness through rigorous sensor testing and characterization. 

NEUROPATCH aims to bridge the gap between clinical-grade cognitive monitoring and accessible, portable solutions for schools, mental health screenings, and personal neurofeedback.

## Sensors Used
| Sensor     | MAX30102             | GSR Sensor v2                 |
| Type       | Optical (PPG)        | Analog (EDA)                  |
| Purpose    | HR, HRV, SpO₂        | Stress / attention monitoring |
| Interface  | I²C                  | Analog                        |
| Power      | 3.3V                 | 3.3 V                         |
| Pins       | SDA → GP0, SCL → GP1 | OUT → GP26 (ADC0)             |

