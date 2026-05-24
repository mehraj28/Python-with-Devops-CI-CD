🚀 Python with DevOps CI/CD

A practical hands-on CI/CD project built using Python Flask, GitHub Actions, Docker-ready architecture, Environment Variables, and Deployment Configuration.

This project demonstrates a complete modern DevOps workflow including:

Source Control Management using Git & GitHub
Continuous Integration using GitHub Actions
Automated Testing using Pytest
Secure Configuration using Environment Variables & GitHub Secrets
Containerization using Docker
Deployment-ready configuration using Heroku
📌 Project Overview

This project simulates a real-world CI/CD implementation for a Python-based web application.

The application is a simple Flask API called TaskFlow API, which supports:

Health monitoring
Environment configuration validation
Task management APIs

The main focus of this project is demonstrating:

CI/CD pipeline automation
Automated testing
DevOps workflows
Deployment preparation
Containerization concepts
🏗️ Tech Stack
Technology	Purpose
Python 3.10	Backend Language
Flask	Web Framework
Pytest	Automated Testing
GitHub Actions	Continuous Integration
Docker	Containerization
Gunicorn	Production WSGI Server
Heroku	Deployment Configuration
Git & GitHub	Source Control
📂 Project Structure
Python-with-Devops-CI-CD/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── tests/
│   ├── __init__.py
│   └── test_app.py
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Procfile
├── runtime.txt
├── .gitignore
├── .env
└── README.md
⚙️ Features Implemented
✅ Flask REST API
Health endpoint
Environment validation endpoint
Task management endpoints
✅ Automated Testing

Implemented automated test cases using Pytest.

Tests Included
Home route validation
Health endpoint validation
✅ Continuous Integration (CI)

Implemented automated CI pipeline using GitHub Actions.

Pipeline Features
Trigger on every push
Install dependencies
Execute automated tests
Validate application integrity
✅ Environment Variables & Secrets Management

Implemented secure configuration using:

.env
GitHub Secrets
Environment Variables Used
Variable	Purpose
APP_ENV	Application environment
SECRET_KEY	Secret configuration
✅ Docker-Ready Architecture

Created Dockerfile for containerized deployment.

Docker Features
Python base image
Dependency installation
Runtime packaging
Deployment-ready configuration
✅ Heroku Deployment Configuration

Prepared deployment configuration using:

Procfile
runtime.txt
🚀 API Endpoints
Endpoint	Method	Description
/	GET	Application status
/health	GET	Health monitoring
/env	GET	Environment validation
/tasks	GET	Retrieve tasks
/tasks	POST	Add new task
🔧 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/mehraj28/Python-with-Devops-CI-CD.git
2️⃣ Navigate to Project
cd Python-with-Devops-CI-CD
3️⃣ Create Virtual Environment
Windows
python -m venv venv
Activate Environment
venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Running the Application

Start Flask server:

python app.py

Application runs at:

http://127.0.0.1:5000
🧪 Running Automated Tests

Execute test suite:

pytest tests/

Expected output:

2 passed
⚡ GitHub Actions CI Pipeline

CI pipeline is configured using:

.github/workflows/python-ci.yml
Pipeline Workflow
Developer Pushes Code
        ↓
GitHub Actions Triggered
        ↓
Install Dependencies
        ↓
Run Automated Tests
        ↓
Build Validation Successful
🔐 Environment Variables

Create .env file:

APP_ENV=development
SECRET_KEY=mysecretkey123
🔒 GitHub Secrets

Secrets configured in:

GitHub Repository
→ Settings
→ Secrets and Variables
→ Actions
Secrets Used
Secret	Purpose
APP_ENV	Deployment environment
SECRET_KEY	Secure secret configuration
🐳 Docker Configuration

Dockerfile created for container-ready deployment.

Build Docker Image
docker build -t taskflow-api .
Run Docker Container
docker run -p 5000:5000 taskflow-api
☁️ Heroku Deployment Configuration

Deployment-ready files included:

Procfile
web: gunicorn app:app
runtime.txt
python-3.10.0
📈 CI/CD Workflow Architecture
Developer Push
      ↓
GitHub Repository
      ↓
GitHub Actions CI Pipeline
      ↓
Install Dependencies
      ↓
Run Automated Tests
      ↓
Validate Build
      ↓
Deployment-Ready Application
🩺 Health Monitoring

Health endpoint:

/health

Example response:

{
  "status": "healthy"
}

This endpoint is useful for:

CI/CD validation
Kubernetes readiness checks
Monitoring systems
Load balancer health checks
🛠️ Troubleshooting
Common Issues
Pytest Not Detecting Tests

Solution:

pytest tests/
Git Push Rejected

Solution:

git pull origin main --allow-unrelated-histories
Environment Variables Not Loading

Ensure:

.env exists
load_dotenv() is added
variable names match correctly
🎯 Learning Outcomes

By completing this project, you will learn:

CI/CD fundamentals
GitHub Actions automation
Automated testing workflows
Docker containerization concepts
Secure secrets management
Deployment architecture
DevOps best practices
📚 Future Improvements

Possible enhancements:

Kubernetes deployment
AWS/GCP deployment
Jenkins pipeline integration
Database integration
API authentication
Production monitoring
Logging system
Multi-stage Docker builds
👨‍💻 Author

Mehraj

GitHub Repository:

Python-with-Devops-CI-CD Repository

⭐ Conclusion

This project demonstrates a practical implementation of modern CI/CD workflows using Python and DevOps practices.

It covers:

Continuous Integration
Automated Testing
Environment Management
Secure Configuration
Containerization
Deployment Preparation