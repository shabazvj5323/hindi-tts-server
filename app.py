from flask import Flask, request, send_file, jsonify
from gtts import gTTS
import io, os, uuid

app = Flask(__name__)

AUDIO_DIR = '/tmp/audio'
os.makedirs(AUDIO_DIR, exist_ok=True)

@app.route('/tts', methods=['POST'])
def tts():
    text = request.json.get('text', '')
    tts = gTTS(text=text, lang='hi')
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(AUDIO_DIR, filename)
    tts.save(filepath)
    audio_url = f"https://hindi-tts-server.onrender.com/audio/{filename}"
    return jsonify({"audio_url": audio_url})

@app.route('/audio/<filename>', methods=['GET'])
def serve_audio(filename):
    filepath = os.path.join(AUDIO_DIR, filename)
    return send_file(filepath, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    
