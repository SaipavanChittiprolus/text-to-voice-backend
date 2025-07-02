import os
from flask import Flask, request, send_file
from flask_cors import CORS
from gtts import gTTS

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return 'Server is running!'

@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    text = data['text']
    lang = data.get('lang', 'en')
    tld = data.get('tld', 'com') 

    tts = gTTS(text=text, lang=lang, tld=tld)
    filename = 'output.mp3'
    tts.save(filename)
    
    return send_file(filename, mimetype='audio/mpeg')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  
    app.run(host='0.0.0.0', port=port)
