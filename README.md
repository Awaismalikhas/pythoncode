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
  ![Screenshot (212)](https://github.com/user-attachments/assets/69de2a4c-298f-43a5-ba7d-59bdd597acf1)
  ![Screenshot (213)](https://github.com/user-attachments/assets/80544047-d161-44e6-8e03-6c06688ce506)
  ![Screenshot (214)](https://github.com/user-attachments/assets/23f9a5e9-6254-4413-ad77-07a1d68c1629)
  ![Screenshot (215)](https://github.com/user-attachments/assets/54ca25f6-41df-4700-9f26-227f911723c6)
  ![Screenshot (216)](https://github.com/user-attachments/assets/84cfa430-7963-4baf-b53d-cb4d4dbcb592)
  ![Screenshot (217)](https://github.com/user-attachments/assets/c345650b-7f91-42f2-84cb-45f9020b8e15)
  ![Screenshot (218)](https://github.com/user-attachments/assets/063bdb42-22ae-46de-a3d0-06a903f29d6b)
  ![Screenshot (219)](https://github.com/user-attachments/assets/9b1dbb94-b7fe-41ef-9279-2adf3b98b389)

 
  



  

  
  


  


