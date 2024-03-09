#Dockerfile for shinyapp

# Dockerfile for shinyapp

# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file to the container
COPY app.py .

# Expose the port on which the app will run
EXPOSE 8080

# Run app on 8050

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]