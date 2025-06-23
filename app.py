from flask import Flask, request, send_file
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def home():
    return 'Server is running!'

@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    text = data['text']
    lang = data.get('lang', 'en')
    tld = data.get('tld', 'com')  # Accent control

    tts = gTTS(text=text, lang=lang, tld=tld)
    filename = 'output.mp3'
    tts.save(filename)
    
    return send_file(filename, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
