from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected for uploading'}), 400
    
    # Đọc ảnh từ file upload
    image = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Nhận diện khuôn mặt
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    number_of_faces = len(faces)
    
    return jsonify({'number_of_faces': number_of_faces})

if __name__ == "__main__":
    app.run(debug=True)
