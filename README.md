# 🤖 KUKA Robotic Pick & Place with IIoT Integration

![License](https://img.shields.io/badge/License-MIT-blue)
![Domain](https://img.shields.io/badge/Domain-Robotics%20%26%20Automation-brightgreen)
![Integration](https://img.shields.io/badge/Integration-IIoT%20(OPC--UA)-orange)
![Tools](https://img.shields.io/badge/Tools-KRL%2C%20RoboDK%2C%20Python-blueviolet)

---

## 📌 Project Overview
This project demonstrates the **programming, simulation, and IIoT integration** of a **KUKA ERS 3.0 robotic arm** to perform a **Pick & Place operation**.  

Developed during my **Robotic Systems Programming & Operation Internship at Otto-von-Guericke University Magdeburg (May 2025 – Ongoing)**, this project goes beyond a basic Pick & Place exercise by showcasing **remote robot operation via OPC-UA and Python**, bridging the gap between **classical robotics** and **Industry 4.0 smart factory concepts**.

---

## ⭐ STAR Contribution

**Situation**  
The task was to automate a Pick & Place sequence on a 6-axis KUKA robotic arm, while also extending the system into an **IIoT-enabled environment** to enable remote, multi-user control.  

**Task**  
- Program the robot using **KUKA Robot Language (KRL)**.  
- Validate motions through **RoboDK simulation** before execution.  
- Establish **OPC-UA connectivity** and integrate Python for real-time remote control.  
- Deliver both a **functional on-site demo** and a **scalable digital workflow**.  

**Action**  
- Built and imported CAD models into **RoboDK** for trajectory simulation and collision detection.  
- Programmed robot movement in **KRL**, tested locally on KUKA Robot Controller (KRC) and SmartPAD.  
- Integrated **OPC-UA server** with a **Python-based client-server system** to enable Industry 4.0 connectivity.  
- Configured **SmartHMI & PLC-level controls** for local testing and fallback.  

**Result**  
- Achieved a **fully automated Pick & Place cycle**, validated in both simulation and on a physical **LEGO-based KUKA ERS 3.0** robot.  
- Enabled **remote, multi-user operation** through OPC-UA and Python integration.  
- Demonstrated strong skills in **robotics programming, IIoT connectivity, PLC systems, and automation integration**.  
- Produced **comprehensive documentation, source code, CAD models, and demo video** for reproducibility.  

---

## 🖼️ Project Highlights

| Stage | Image |
|-------|-------|
| **1. RoboDK Simulation** | ![Simulation](docs/figures/01_RoboDK_Simulation.jpg) |
| **2. SmartPAD & KRL Programming** | ![SmartPAD](docs/figures/02_KRL_SmartPAD.jpg) |
| **3. Physical Robot Execution** | ![Robot](docs/figures/03_Physical_Robot.jpg) |

---

## 📂 Repository Structure

---

## 📑 Reports & Documentation
- 📘 **KUKA Pick & Place Guide (PDF):** [KUKA_PickPlace_Guide.pdf](docs/reports/KUKA_PickPlace_Guide.pdf)  
  *(includes step-by-step workflow, screenshots, and technical explanations)*

---

## 💻 Source Code
- 📝 **KUKA Pick & Place Program:** [kuka_pick_and_place.src](src/kuka_pick_and_place.src)

---

## 📹 Demo Video
🎥 [Watch Pick & Place Execution Demo](media/kuka_pick_place_demo.mp4)  
 

---

## 🗂️ CAD Models & Simulation Assets
To keep the repository lean, the **full CAD package** is provided as a downloadable Release:  

👉 [Download KUKA ERS 3.0 CAD Models (WRL, STEP, IGES)](../../releases/latest/download/KUKA_ERS3.0_FullModels_v1.0.zip)

Contents include:  
- ERS3.0 assembly & parts (`.wrl`, `.iges`, `.step`)  
- RoboDK project setup (`.rdk`)  
- Robot workspace layouts  

---

## 🛠️ Tools & Technologies
- **KUKA Robot Language (KRL)** – trajectory programming  
- **KUKA Robot Controller (KRC) & SmartPAD/SmartHMI** – on-site testing  
- **RoboDK** – offline programming and collision-free simulation  
- **OPC-UA** – robot-to-cloud communication protocol  
- **Python (Client-Server)** – remote, multi-user control integration  
- **PLC Interfaces** – local control and safety redundancy  

---

## 🔑 Key Takeaways
- Delivered a **working robotic system** that integrates **classical programming + Industry 4.0 remote control**.  
- Showcased the **end-to-end robotics workflow**: CAD models → simulation → programming → physical execution → remote operation.  
- Provided a **recruiter-friendly demonstration** of skills in **robotics, automation, IIoT, and digital manufacturing**.  
- This project reflects my ability to **bridge hardware, software, and connectivity layers** in real-world robotic systems.  

---

## ⚖️ License
Distributed under the [MIT License](LICENSE).
