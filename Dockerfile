FROM python:3.9-slim

WORKDIR /app

# Install system dependencies required for LightGBM
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Make sure the model directory exists
RUN mkdir -p artifacts/models

# Expose the port the app runs on
EXPOSE 7860

# Command to run the application
CMD ["python", "app.py"]