# Use an official Python image
FROM python:3.13-slim

# Set Working Directory
WORKDIR /app

# Copy Project files
COPY requirements.txt .
COPY app.py .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the flask port
EXPOSE 5000

# Run the flask app
cmd ["python","app.py"]

