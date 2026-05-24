from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV=os.getenv('APP_ENV')
SECRET_KEY=os.getenv('SECRET_KEY')

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return jsonify({"message": "TaskFlow API Running"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    tasks.append(data)

    return jsonify({
        "message": "Task Added",
        "task": data
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/env')
def env():
    return jsonify({
        "environment": APP_ENV,
        "secret_loaded": SECRET_KEY is not None
    })

if __name__ == '__main__':
    app.run(debug=True)