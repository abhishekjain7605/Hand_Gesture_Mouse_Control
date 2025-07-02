# 🖐️ Hand Gesture Mouse Control

Control your computer mouse using hand gestures detected through your webcam! This project uses Python, OpenCV, MediaPipe, and Flask to create a virtual mouse interface. The gestures are processed in real-time and translated into mouse actions like move, click, scroll, and drag.

---

## 🚀 Features

* Real-time hand tracking with MediaPipe
* Cursor movement with index finger
* Left-click, right-click, and drag gestures
* Scroll with hand movements
* Web-based interface using Flask
* MongoDB integration for logging or analytics

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/hand-gesture-mouse-control.git
cd hand-gesture-mouse-control
```

2. **Install Required Packages**

```bash
pip install -r requirements.txt
```

> Or manually install them:

```bash
pip install Flask flask-cors pymongo werkzeug opencv-python mediapipe pyautogui
```

3. **Ensure MongoDB is Running**

Make sure your MongoDB service is up and running locally (default: `mongodb://localhost:27017/`).

4. **Run the Flask App**

```bash
python app.py
```

5. **Access the App**

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

* The webcam captures real-time video.
* MediaPipe detects hand landmarks.
* Specific finger gestures are mapped to mouse actions.
* Flask serves a local web application, and MongoDB logs interactions.

---

## 🧪 Use Cases

* Hands-free PC control
* Accessibility tool
* Educational projects in Computer Vision
* Fun tech demo for CV/AI portfolio

---

## 📝 To-Do / Future Enhancements

* Add multi-hand support
* Gesture customization UI
* Deploy as a desktop app with PyInstaller
* Remote mouse control via web/mobile

---

## 🤝 Contributing

Feel free to fork this repo and open pull requests. Contributions are welcome!

---
