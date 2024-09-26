from flask import Flask, send_file
import pyqrcode

app = Flask(__name__)

@app.route('/')
def generate_qr():
    s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
    url = pyqrcode.create(s)
    url.png("myqr.png", scale=8)
    return send_file("myqr.png", mimetype="image/png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
