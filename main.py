# main.py
import cv2
import pandas as pd
from datetime import datetime
from deepface import DeepFace
import os

# Path to employee images
path = "EmployeeImages"
employee_images = os.listdir(path)
employee_names = [os.path.splitext(f)[0] for f in employee_images]

# Initialize webcam
cap = cv2.VideoCapture(0)

# Ensure attendance file exists
if not os.path.exists("attendance.csv"):
    pd.DataFrame(columns=["Name", "Date", "Time"]).to_csv("attendance.csv", index=False)

def mark_attendance(name):
    df = pd.read_csv("attendance.csv")
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if not ((df["Name"] == name) & (df["Date"] == date)).any():
        new_entry = pd.DataFrame([[name, date, time]], columns=["Name", "Date", "Time"])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv("attendance.csv", index=False)

print("Starting webcam... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save a temporary frame
    cv2.imwrite("temp.jpg", frame)

    # Loop through each employee image to check
    for emp_image, emp_name in zip(employee_images, employee_names):
        try:
            result = DeepFace.verify(
                img1_path="temp.jpg",
                img2_path=os.path.join(path, emp_image),
                enforce_detection=False
            )
            if result["verified"]:
                mark_attendance(emp_name)
                cv2.putText(frame, emp_name, (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except:
            continue

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
