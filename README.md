# 🅿️ Automatic Vacancy Slot Detection System

This project implements a Parking Slot Detection system using object detection techniques to identify whether parking slots in a video are **occupied** or **vacant**.

---

## 🔍 What the Project Does

- Extracts frames from a parking lot video to build the dataset  
- Allows manual selection of parking slot positions on a reference image  
- Detects vehicles in each video frame using YOLOv5  
- Compares detected vehicle positions with predefined parking slots to determine their status  
- Visualizes detection results using color-coded rectangles:  
  - 🟥 **Red** – Occupied  
  - 🟩 **Green** – Free  
- Displays a real-time counter overlay showing:  
  `Free: X / Total`


## 🛠️ Tech Stack

- **Python**
- **OpenCV** – Video processing and visualization  
- **PyTorch** – Deep learning framework  
- **YOLOv5** – Object detection for vehicle recognition  


