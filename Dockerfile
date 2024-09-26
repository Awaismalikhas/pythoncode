FROM python:3.9-slim

WORKDIR /app
RUN pip install pyqrcode pypng flask
COPY /simplepythonapp/app.py .
EXPOSE 5000
CMD ["python", "app.py"]
