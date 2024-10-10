from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

NODE_SERVER_URL = 'http://localhost:3000'  # Cambia la URL si es necesario

@app.route('/upload', methods=['POST'])
def upload_video():
    video = request.files['video']
    if video:
        # Enviar el video al backend de Node.js
        response = requests.post(f"{NODE_SERVER_URL}/upload", files={'video': video})
        return jsonify({"message": response.text}), response.status_code
    return jsonify({"error": "No se proporcionó video"}), 400

@app.route('/videos/<filename>', methods=['GET'])
def get_video(filename):
    video_url = f"{NODE_SERVER_URL}/videos/{filename}"
    return requests.get(video_url).content

if __name__ == '__main__':
    app.run(port=5000)
