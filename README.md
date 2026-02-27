# Facial Recognition Employee Attendance System

## Project Overview
This project is a **Facial Recognition Employee Attendance System** that automatically records employee attendance using AI-based face recognition technology.  
It eliminates the need for manual entry or biometric devices, ensures only authorized personnel can mark attendance, and provides real-time attendance data for better workforce management.

## Features
- **Automatic Attendance** – Employees are recognized automatically via face recognition.
- **Secure** – Only authorized personnel can mark attendance, reducing proxy or fraudulent entries.
- **Real-Time Reporting** – View attendance records instantly.
- **Easy to Use** – Just place employee images in the `EmployeeImages` folder and run the system.

## Project Structure

Hexsoftwares_Facial_Recog_Emp_Att_System/

├── EmployeeImages/      # Folder containing employee photos

├── attendance.csv       # Attendance records

├── main.py              # Main program to run the system

└── README.md            # Project description

## Installation
1. Make sure you have **Python 3.11** installed.
2. Install required libraries:
pip install opencv-python deepface pandas

> This version uses **DeepFace** for face recognition, which works on Python 3.11 without requiring dlib.

## How to Use
1. Place all employee images in the `EmployeeImages` folder.
2. Run the system:
python main.py

3. The system will automatically detect faces and mark attendance in `attendance.csv`.

## Contribution
If you want to contribute, fork the repository, make changes, and create a pull request.

## License
This project is for educational purposes. You can use and modify it freely.

