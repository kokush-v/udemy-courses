import os
from PyPDF2 import PdfReader
from flask import abort, jsonify, request
from gtts import gTTS
from app import app


def generate_speech(text: str, lang: str) -> str:
    tts = gTTS(text=text, lang=lang)
    name = f"{text.split(' ')[0]}.mp3"
    tts.save(name)
    return name


def get_pdf_file() -> str:
    if 'file' not in request.files:
        abort(400, description="No file part in the request")

    file = request.files['file']
    if file.filename == '' or not file.filename.endswith('.pdf'):
        abort(400, description="Invalid file type. Please upload a PDF.")

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return file_path


def parse_pdf_file(file_path: str) -> str:
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        os.remove(file_path)
        return text
    except Exception as e:
        os.remove(file_path)
        abort(500, description=str(e))
