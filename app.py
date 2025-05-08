import os
from flask import Flask

app = Flask(__name__)
MESSAGE = os.getenv("APP_MSG", "🚀 Hello from Dockerized Flask App!")

@app.route('/')
def home():
    return MESSAGE

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
