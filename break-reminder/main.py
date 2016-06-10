import threading
import webview
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "hhhhejloo"


if __name__ == "__main__":
    flask_thread = threading.Thread(target=app.run)
    flask_thread.daemon = True
    flask_thread.start()

    webview.create_window("hello", "http://127.0.0.1:5000")
