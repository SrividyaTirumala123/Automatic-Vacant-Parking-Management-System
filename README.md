# Automatic Vacancy Slot Detection System

This project employs Python, OpenCV, and PyTorch to detect and classify parking slots in video streams determining whether each slot is occupied or vacant.

---

##  About

- Extracts frames from a parking lot video to build the dataset  
- Allows manual selection of parking slot positions on a reference image  
- Detects vehicles in each video frame using YOLOv5  
- Compares detected vehicle positions with predefined parking slots to determine their status  
- Visualizes detection results using color-coded rectangles:  
  - 🟥 **Red** – Occupied  
  - 🟩 **Green** – Free  
- Displays a real-time counter overlay showing:  
  `Free: X / Total`




