# Automatic Vacancy Slot Detection System

This project implements a Parking Slot Detection system using the pretrained **YOLOv5** model for vehicle detection combined with custom logic to detect whether parking slots are occupied or free.

---

## 🔍 What the Project Does

- Extracts frames from a parking lot video to build the dataset.  
- Allows manual selection of parking slot positions on an image.  
- Utilizes a pretrained YOLOv5s model to detect vehicles in each video frame.  
- Compares detected vehicle positions with predefined parking slots to determine whether they are occupied or vacant.  
- Visualizes the detection results using color-coded rectangles:  
  - 🟥 **Red:** Occupied  
  - 🟩 **Green:** Free  
- Displays a real-time counter on video frames showing:  
  `Free: X / Total`

---

## 🤔 Why use a pretrained model?

- Using a pretrained model allows quick deployment and demonstration of parking detection functionality without the overhead of time-consuming custom training.  
- It is an effective approach for proof of concept and applications where the pretrained model generalizes well.

---

## 📈 Current Status

- The project includes scripts for extracting frames and preparing datasets.  
- Initial efforts towards training a custom YOLOv5 model were made to enhance detection accuracy.  
- Currently, the system uses the pretrained YOLOv5 model for reliable and fast inference.  
- Custom training and fine-tuning remain as exciting future improvements to further tailor the model to this specific parking environment.

