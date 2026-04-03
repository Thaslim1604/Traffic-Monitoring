from flask import Flask, render_template, Response, jsonify
import cv2
import threading
from detector import process_frame

app = Flask(__name__)

VIDEO_PATH = 'traffic.mp4'

latest_stats = {
    'total': 0,
    'cars': 0,
    'trucks': 0,
    'buses': 0,
    'bikes': 0,
    'density': 'Low'
}
stats_lock = threading.Lock()

def generate_frames():
    cap = cv2.VideoCapture(VIDEO_PATH)
    while True:
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # loop video
            continue

        frame = cv2.resize(frame, (960, 540))
        processed_frame, counts, total, density = process_frame(frame)

        with stats_lock:
            latest_stats['total'] = total
            latest_stats['cars'] = counts['Car']
            latest_stats['trucks'] = counts['Truck']
            latest_stats['buses'] = counts['Bus']
            latest_stats['bikes'] = counts['Motorcycle']
            latest_stats['density'] = density

        ret, buffer = cv2.imencode('.jpg', processed_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stats')
def stats():
    with stats_lock:
        return jsonify(latest_stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)