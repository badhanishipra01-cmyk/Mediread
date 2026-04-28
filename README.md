# MediRead AI

MediRead AI is a prototype that converts handwritten medical prescriptions into readable text and predicts medicine names using OCR and fuzzy matching.

## Features
- Upload prescription image
- Extract handwritten text (EasyOCR)
- Intelligent medicine detection (Fuzzy Matching)
- Confidence score for predictions

## Technologies Used
- Python
- Flask
- EasyOCR
- FuzzyWuzzy
- HTML

## How to Run
1. Install dependencies:
   pip install flask easyocr opencv-python numpy fuzzywuzzy python-Levenshtein

2. Run the app:
   python app.py

3. Open browser:
   http://127.0.0.1:5000/

## Future Improvements
- Better handwriting recognition using AI models
- Mobile app version
- Multi-language support
