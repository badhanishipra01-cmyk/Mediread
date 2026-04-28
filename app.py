from flask import Flask, render_template, request
import easyocr
import os
from fuzzywuzzy import fuzz

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

reader = easyocr.Reader(['en'], gpu=False)

# Load medicine list
with open("medicines.txt", "r") as f:
    medicines = [line.strip().lower() for line in f]


# ✅ IMPROVED MATCHING FUNCTION
def match_medicines(text):
    results = []
    text = text.lower()

    for med in medicines:
        score1 = fuzz.ratio(text, med)
        score2 = fuzz.partial_ratio(text, med)
        score3 = fuzz.token_sort_ratio(text, med)

        score = max(score1, score2, score3)

        results.append((med, score))

    # sort by best match
    results = sorted(results, key=lambda x: x[1], reverse=True)

    # return top 3 matches
    return results[:3]


@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = ""
    found_meds = []

    if request.method == "POST":
        file = request.files["image"]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # OCR
        result = reader.readtext(filepath, detail=0)
        extracted_text = " ".join(result).lower()

        # Match medicines
        found_meds = match_medicines(extracted_text)

    return render_template("index.html", text=extracted_text, meds=found_meds)


if __name__ == "__main__":
    app.run(debug=True)