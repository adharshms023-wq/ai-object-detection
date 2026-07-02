# 🛡️ Smart AI CCTV Surveillance System

A real-time AI-powered CCTV surveillance system built using **Python**, **OpenCV**, and **YOLOv8**. The application detects multiple objects from a live camera feed, displays confidence scores, tracks object statistics, and provides a modern surveillance dashboard.

---

## 📸 Features

* 🎯 Real-time object detection using YOLOv8
* 👤 Detects all 80 COCO dataset object classes
* 📊 Confidence percentage for every detection
* 📈 Colored confidence bars
* 🟢 Live FPS monitoring
* 📋 Object statistics dashboard
* 🎥 Webcam support
* 🖥️ Full-screen display mode
* 🎨 Modern AI CCTV interface
* ⚡ Fast inference with Ultralytics YOLO

---

## 🖼️ Dashboard

The application displays:

* Smart AI CCTV title
* FPS counter
* System status
* Total detected objects
* Live object count
* Confidence percentage
* Confidence bars
* Colored bounding boxes

Example:

```
SMART AI CCTV

FPS : 30
Status : ONLINE

Detected Objects
-----------------------
Person : 2
Laptop : 1
Bottle : 3
Chair : 4
```

---

## 🛠️ Technologies Used

* Python 3.x
* OpenCV
* Ultralytics YOLOv8
* NumPy

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/adharshms023-wq/ai-object-detection.git
cd ai-object-detection
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

---

## 📂 Project Structure

```
ai-object-detection/
│
├── main.py
├── requirements.txt
├── README.md
├── screenshots/
├── models/
└── venv/
```

---

## 📋 Requirements

```
opencv-python
ultralytics
numpy
```

Generate automatically:

```bash
pip freeze > requirements.txt
```

---

## 🚀 Future Improvements

* Multi-object tracking (ByteTrack)
* Restricted zone alerts
* Intrusion detection
* Face recognition
* License plate recognition
* Email and Telegram alerts
* Video recording
* Snapshot capture
* Web dashboard using Flask/FastAPI
* Database logging
* IP Camera (RTSP) support
* Cloud deployment
* Mobile dashboard

---

## 💡 Applications

* Smart Surveillance
* Office Security
* Home Monitoring
* Warehouse Monitoring
* Classroom Monitoring
* Retail Analytics
* Industrial Safety

---

## 🤝 Contributions

Contributions, suggestions, and feature requests are welcome.

Fork the repository, create a new branch, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Adharsh M S**

GitHub:
https://github.com/adharshms023-wq
