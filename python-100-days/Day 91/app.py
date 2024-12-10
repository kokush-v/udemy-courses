import os
from flask import Flask, request, send_file
from util import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs('uploads', exist_ok=True)


@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    lang_code = request.args.get("lang", "en")
    file_path = get_pdf_file()
    text_from_pdf = parse_pdf_file(file_path)
    audio = generate_speech(text=text_from_pdf, lang=lang_code)
    return send_file(audio, mimetype="audio/mpeg", as_attachment=True, download_name="speech.mp3")


if __name__ == '__main__':
    app.run(debug=True)
