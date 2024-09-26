# Python Flask QR Code Generator with CI/CD Pipeline

This project is a Python Flask web application that generates a QR code . It includes a Dockerfile for containerization and a Jenkins pipeline for automating the CI/CD process.

## Features

- **QR Code Generation**: The web app generates a QR code 
- **Containerization**: The application is containerized using Docker.
- **CI/CD Pipeline**: A Jenkins pipeline is used to automate the process of cloning, building, and deploying the Dockerized application.

## Project Structure

- **app.py**: Flask application that generates and serves the QR code.
- **Dockerfile**: Contains instructions to build a Docker image for the application.
- **Jenkinsfile**: Defines the pipeline stages for continuous integration and deployment.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker
- Jenkins (for CI/CD pipeline)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Awaismalikhas/pythoncode.git
   
 ###  Install required Python packages:
pip install pyqrcode pypng flask

 ###     Run the Flask app locally:
python app.py
 ###    To run the app in a Docker container:
docker build -t pythonapplicationhai .

docker run -d -p 5000:5000 pythonapplicationhai

  ### Here are images of the output 
 
  



  

  
  


  


