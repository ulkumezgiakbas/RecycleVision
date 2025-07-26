# RecycleVision ♻️

RecycleVision is a real-time object detection project focused on identifying recyclable materials using YOLOv8. It detects 7 types of waste: **Cardboard, Garbage, Glass, Metal, Paper, Plastic, Trash**. The goal is to support recycling efforts by providing fast and accurate classification through a live camera feed.

## 🚀 Features
- YOLOv8n-based lightweight model
- Real-time detection via webcam
- Trained on Roboflow dataset with 7 waste categories
- Outputs bounding boxes with confidence scores

## 📁 Project Structure
RecycleVision/
│
├── live_detect.py # Main live webcam detection script
├── data.yaml # Dataset configuration file
├── yolov8n.pt # Pretrained YOLOv8n weights (optional)
├── dataset/ # Contains train/val/test images and labels
├── runs/ # YOLO inference and training outputs


## 🧠 Model Info
- Model: YOLOv8n
- Epochs: 20
- Input Size: 640x640
- Trained with Ultralytics library
- CPU-compatible (Apple M2 tested)

## 📷 Example Results
![WhatsApp Image 2025-07-26 at 22 10 29](https://github.com/user-attachments/assets/291e92ab-5e27-4b75-8b42-69aa9e2659d3)


## 🛠️ How to Run

### Live Detection via Webcam
python live_detect.py


*Requirements
Python 3.10+

Ultralytics (YOLOv8)

OpenCV


⚖️ License
This project is licensed under the MIT License — feel free to use and modify it.

Made by Ezgi Akbaş
