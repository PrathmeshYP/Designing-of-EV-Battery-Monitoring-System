# Designing of EV Battery Monitoring System ⚡🔋

## 📘 Project Overview
The **EV Battery Monitoring System** is a microcontroller-based solution designed to monitor and evaluate the health and performance of electric vehicle (EV) batteries in real time. The system focuses on accurate measurement of critical battery parameters such as **voltage, current, temperature, State of Charge (SOC), and State of Health (SOH)**.

This project provides a **cost-effective and reliable alternative** to complex commercial Battery Management Systems (BMS), making it suitable for **educational, research, and small-scale EV applications**.

---

## 🧠 Problem Statement
In EV battery packs, variations in cell voltage, temperature, and SOC cause imbalance, performance degradation, and safety risks. Conventional low-cost BMS solutions lack accurate real-time monitoring and early fault detection.

This project addresses the need for a **simple, affordable, and reliable battery monitoring system** capable of continuously tracking battery parameters and detecting abnormal conditions without complex circuitry.

---

## 🎯 Objectives
- Real-time monitoring of voltage, current, temperature, SOC, and SOH  
- Early detection of faults such as overheating, overcurrent, and voltage imbalance  
- Accurate data processing using a microcontroller-based system  
- Clear and user-friendly real-time data display using an LCD  
- Performance validation across different EV battery types  

---

## 🔍 Scope of the Project
- Development of a real-time EV battery monitoring unit  
- Integration of voltage, current, and temperature sensors  
- Testing on multiple EV battery chemistries and capacities  
- Evaluation of system accuracy, reliability, and repeatability  

---

## 🛠️ System Architecture
![WhatsApp Image 2025-12-08 at 9 24 20 AM](https://github.com/user-attachments/assets/4ff3c9ca-2040-4f2d-b2ca-da01543f4c4c)
The system consists of:
- **Microcontroller:** Arduino Uno  
- **Voltage Sensor:** Voltage Divider Module (VM427)  
- **Current Sensor:** ACS712
- **Temperature Sensor:** DS18B20  
- **Display Unit:** 16×2 LCD with I2C interface  

The sensors continuously collect battery data, which is processed by the microcontroller and displayed in real time.

---

## 🔬 Methodology
1. **Sensor-Based Data Acquisition**  
   Continuous measurement of voltage, current, and temperature under various operating conditions.

2. **Signal Conditioning & Processing**  
   Calibration, filtering, and scaling of sensor signals to improve accuracy.

3. **Microcontroller Logic Development**  
   Real-time computation of SOC and SOH and detection of abnormal operating conditions.

4. **Real-Time Display**  
   Live battery parameters displayed on LCD without external software.

5. **Experimental Validation**  
   Performance testing using controlled discharge and load conditions.

---

## 📊 Results Summary
| Parameter    | Observed Performance              | Accuracy |
|--------------|-----------------------------------|----------|
| Voltage      | Stable during discharge           | ±1%      |
| Current      | Instant response to load changes  | ±1.5%    |
| Temperature  | Accurate heat detection           | ±0.5°C   |
| SOC          | Smooth and consistent estimation  | Reliable |

---

## ✅ Key Outcomes
- Accurate real-time battery parameter monitoring  
- Reliable SOC estimation for small EV batteries  
- Effective fault detection and protection logic  
- Suitable for low-cost EV and educational applications  

---

## 💡 Advantages
- Low-cost and simple hardware design  
- Open-source and easily customizable  
- Real-time monitoring without complex BMS circuitry  
- Compatible with multiple EV battery types  

---

## 🚀 Future Enhancements
- Wireless data transmission  
- Data logging and cloud monitoring  
- Advanced SOC/SOH estimation algorithms  
- Integration with full EV Battery Management Systems  

---

## 📌 Applications
- Electric Vehicles (EVs)  
- Battery testing laboratories  
- Educational and research projects  
- Prototype EV systems  


