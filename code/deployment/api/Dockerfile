# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY code/deployment/api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY code/datasets ./datasets
COPY code/deployment/api/api.py ./api.py
COPY code/models ./models_code
COPY /models ./models

EXPOSE 8000

CMD ["python", "api.py"]
