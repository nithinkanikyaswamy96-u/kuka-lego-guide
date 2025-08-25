# KUKA Robotics – Pick & Place (Guide + IIoT)

<p align="left">
  <img src="https://img.shields.io/badge/Focus-Robotics-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tools-KUKA%20KRC%20%7C%20RoboDK%20%7C%20Python-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge" />
</p>

Robot programming for pick-and-place and an **OPC-UA + Python** IIoT concept for remote supervision/control.  
*Note:* OPC-UA licensed assets are **not** shared here; only the interface concept/spec is documented.

---

## ⭐ STAR Summary
- **Situation:** Need to automate repetitive pick-and-place with transparent cell status.
- **Task:** Implement KUKA motion logic (KRL) and define an IIoT interface contract for remote access.
- **Action:** Structured KRL modules (approach/pick/place/retreat), state machine, error handling; specified Python client commands & telemetry over OPC-UA.
- **Result:** Clean, reusable program structure and documented integration concept; expected **~15% cycle efficiency** in repetitive handling.

---

## 🖼️ Highlights
![Cell Overview](docs/figures/cell-overview.png)
![State Machine](docs/figures/state-machine.png)

---

## 📂 Repository Map
- `src/krl/` – sample KRL snippets
- `src/python/` – client spec/examples (no licensed code)
- `docs/reports/` – guide (sanitized)
- `docs/figures/` – cell / teaching points / state diagram
- `LICENSE` – MIT
