# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY deployment/api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY datasets ./datasets
COPY deployment/api/apy.py ./apy.py
COPY models ./models
COPY ../models ./models

EXPOSE 8000

#CMD ["python", "api.py"]
