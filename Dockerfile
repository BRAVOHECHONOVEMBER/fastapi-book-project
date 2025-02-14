# Using the official Python image
FROM python:3.12-slim

# Setting the working directory
WORKDIR /app

# Installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying the application code
COPY . .

# Exposing port 8080
EXPOSE 8080

# Running the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
