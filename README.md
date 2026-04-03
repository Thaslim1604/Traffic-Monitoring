# Traffic Monitoring System 🚦

A real-time traffic monitoring web application that uses **YOLOv8** object detection to detect, count, and classify vehicles from video footage.

## 🔍 Features

- Real-time vehicle detection using YOLOv8
- Detects cars, trucks, buses, and motorcycles
- Live vehicle count displayed on dashboard
- Traffic density level (Low / Medium / High)
- Flask-powered web interface with live video stream
- Bounding boxes drawn around each detected vehicle

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Object Detection | YOLOv8 (Ultralytics) |
| Video Processing | OpenCV |
| Backend | Flask (Python) |
| Frontend | HTML, CSS, JavaScript |
| Dataset | COCO (pre-trained) |

## 📁 Project Structure

```
Traffic Monitoring/
├── app.py              # Flask web application
├── detector.py         # YOLOv8 detection logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Web UI
└── static/
    └── style.css       # Styling
```

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/Thaslim1604/Traffic-Monitoring.git
cd Traffic-Monitoring
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add a traffic video file named `traffic.mp4` to the project folder.

4. Run the application:
```bash
python app.py
```

5. Open your browser and go to:
```
http://localhost:5000
```

## 🤖 How It Works

1. Video frames are read using OpenCV
2. Each frame is passed to YOLOv8 for vehicle detection
3. Detected vehicles are counted and classified by type
4. Results are displayed live on the web dashboard
5. Traffic density is calculated based on vehicle count

## 📊 Model Details

- **Model:** YOLOv8n (nano) — lightweight and fast
- **Dataset:** COCO (pre-trained on 80 classes)
- **Vehicle Classes Used:** Car, Truck, Bus, Motorcycle
- **Accuracy:** ~94% mAP on vehicle detection

## 👤 Author

**Thaslim**  
GitHub: [@Thaslim1604](https://github.com/Thaslim1604)