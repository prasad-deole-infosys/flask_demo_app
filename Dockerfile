# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Command to run the app using gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
