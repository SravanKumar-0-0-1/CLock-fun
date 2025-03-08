# CLock-fun
## ⏰ Clock Applications (Digital Clock & Stopwatch)

## Overview
This repository contains two clock-based applications built with **PyQt5**:
1. **Digital Clock** – A real-time digital clock displaying hours, minutes, and seconds.
2. **Stopwatch** – A functional stopwatch with Start, Stop, and Reset buttons.

Both applications use a **custom digital font (DS-DIGIT.TTF)** and a stylish graphical interface.

## Table of Contents
- [Digital Clock](#digital-clock)
- [Stopwatch](#stopwatch)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

---

## 🕒 Digital Clock
**File:** `Digital_clock.py`

### Features:
- Displays the current time in **HH:MM:SS AM/PM** format.
- Updates automatically every **300 milliseconds**.
- Uses a **custom digital font** for a sleek appearance.
- Black background with **green neon digits**.

### How It Works:
- Uses `QTime.currentTime()` to fetch real-time clock data.
- Updates the label every **300ms** using a `QTimer`.
- Uses **PyQt5's QLabel** to display the clock.

---

## ⏱️ Stopwatch
**File:** `StopWatch.py`

### Features:
- Displays elapsed time in **HH:MM:SS:MS** format.
- Three functional buttons:
  - **Start**: Begins counting time.
  - **Stop**: Pauses the timer.
  - **Reset**: Resets the timer to `00:00:00:00`.
- Stylish design with a **black background and neon green digits**.

### How It Works:
- Uses `QTimer` to increment time every **10 milliseconds**.
- The `QTime` class manages time calculations.
- Buttons are connected to respective functions for control.

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
Make sure you have **Python 3.x** and **PyQt5** installed:
```sh
pip install PyQt5
```

### 2️⃣ Run a Script
To run any clock application, use:
```sh
python filename.py
```
For example:
```sh
python Digital_clock.py
python StopWatch.py
```

---

## 🛠 Requirements
- **Python 3.x**
- **PyQt5**
- **Custom Font (DS-DIGIT.TTF)** (Ensure it is in the same directory)

---

## 🖼️ Screenshots
![Screenshot 2025-03-08 133159](https://github.com/user-attachments/assets/ee6c319c-70e7-403f-bdfb-e2390b405d1c)
![Screenshot 2025-03-08 133439](https://github.com/user-attachments/assets/bd9cf010-5dca-4595-9fc3-ba646ebe7300)


---

## 🤝 Contributing
Feel free to **fork** this repository and enhance the clock applications!

📌 **Enjoy Coding!** 🚀

