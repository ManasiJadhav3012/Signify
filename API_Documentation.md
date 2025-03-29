# 📌 ASL Translator API Documentation
This document provides details about the API endpoints for the ASL Translator Web Application, built using Flask and MediaPipe.

## 📍 Base URL
```bash
http://localhost:5000
```

## 🎯 Get Random Letter (Target Sign)
This endpoint generates a random English alphabet letter (A–Z) that the user should try to sign.

#### ➤ Endpoint:
``` bash
POST /get_random_letter
```

#### ➤ Response (200 OK):
```bash
{
  "random_char": "V"
}
```
No request body is needed.

## 🤖 Predict Probability from Video Frame
This endpoint takes a base64-encoded image frame from the webcam and returns:

    • Probability of sign match (or No hand detected)
    • Bounding box (if a hand is detected)

#### ➤ Endpoint:
```bash
POST /predict_prob
```

#### ➤ Request Body (JSON):
```bash
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA..."
}
```
**🔍 The image should be a base64-encoded PNG frame captured from the video element.**

#### ➤ Response (200 OK):
If a hand is detected:
```bash
{
  "probability": "0.89",
  "bbox": {
    "xmin": 132,
    "ymin": 80,
    "xmax": 260,
    "ymax": 230
  }
}
```
If no hand is detected:
```bash
{
  "probability": "No hand detected"
}
```

## 🖼️ UI Pages (HTML)
These pages are served by the Flask backend:

#### ➤ Home Page
```bash
GET /
```

    • Displays welcome message and buttons for translation modes.

#### ➤ ASL to English (Webcam Prediction UI)
```bash
GET /camera
```

    • Starts webcam.
    • User signs a letter.
    • App detects hand pose and predicts the letter.

#### ➤ English to ASL (Letter-to-Gesture Display)
```bash
GET /english_to_asl
```

    • User inputs a letter.
    • App displays gesture image/animation for that letter.

## ⚠️ Error Handling

If a request is malformed or the image is missing:
``` bash
{
  "error": "Invalid request data"
}
```

If the MediaPipe model fails to detect a hand:
```bash
{
  "probability": "No hand detected"
}
```