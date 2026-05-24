from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
from flasgger import Swagger

# Load environment variables
load_dotenv()

APP_ENV = os.getenv('APP_ENV')
SECRET_KEY = os.getenv('SECRET_KEY')

# Initialize Flask app
app = Flask(__name__)

# Initialize Swagger
Swagger(app)

# Temporary in-memory storage
tasks = []


@app.route('/')
def home():
    """
    Home Endpoint
    ---
    responses:
      200:
        description: Application running successfully
    """
    return jsonify({
        "message": "TaskFlow API Running Successfully"
    })


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Get All Tasks
    ---
    responses:
      200:
        description: Returns all tasks
    """
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Add New Task
    ---
    parameters:
      - name: task
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string

    responses:
      200:
        description: Task added successfully
    """

    data = request.json

    tasks.append(data)

    return jsonify({
        "message": "Task Added Successfully",
        "task": data
    })


@app.route('/health')
def health():
    """
    Health Check Endpoint
    ---
    responses:
      200:
        description: Application health status
    """
    return jsonify({
        "status": "healthy"
    })


@app.route('/env')
def env():
    """
    Environment Information
    ---
    responses:
      200:
        description: Returns environment details
    """
    return jsonify({
        "environment": APP_ENV,
        "secret_loaded": SECRET_KEY is not None
    })


if __name__ == '__main__':
    app.run(debug=True)