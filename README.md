# ASL Translator 🤟

Welcome to the ASL Translator! This web application enables two-way communication between American Sign Language (ASL) and English using real-time video input and deep learning models.

## 🌐 Features

- 🔤 Translate ASL hand signs to English letters using webcam input.
- 📝 Generate random letters for users to mimic using ASL.
- 🔁 Two modes: 
  - ASL to English (via webcam)
  - English to ASL (display animated signs)

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Model**: CNN-based image classification for ASL letters
- **Libraries**: OpenCV, NumPy, Flask, TensorFlow/Keras

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/yourusername/asl-translator.git
cd asl-translator
pip install -r requirements.txt
```

### Run the app

```bash
python app.py
```

### Open your browser and go to:

```bash
http://127.0.0.1:5000
```