---
title: Hotel Reservation Prediction
emoji: 🏨
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "3.9"
app_file: app.py
pinned: false
---

# Hotel Reservation Prediction

This is a Flask web application that predicts whether a hotel reservation will be canceled or not based on various features.

## Project Structure

- `application.py`: Main Flask application file
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration for deployment
- `artifacts/models/`: Directory containing the trained model
- `templates/`: HTML templates for the web interface
- `static/`: CSS and other static files
- `config/`: Configuration files for the application

## Deployment to Hugging Face Spaces

### Prerequisites

1. A Hugging Face account
2. Git installed on your local machine
3. The trained model file (`lgbm_model.pkl`) in the `artifacts/models/` directory

### Deployment Steps

1. Create a new Space on Hugging Face:
   - Go to https://huggingface.co/spaces
   - Click on "Create new Space"
   - Choose a name for your Space
   - Select "Docker" as the SDK
   - Choose public or private visibility
   - Click "Create Space"

2. Clone the Space repository:
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   ```

3. Copy your project files to the cloned repository:
   ```bash
   # Copy all necessary files
   cp -r * /path/to/cloned/repo/
   ```

4. Push the changes to Hugging Face:
   ```bash
   cd /path/to/cloned/repo
   git add .
   git commit -m "Initial commit"
   git push
   ```

5. Your application will be automatically built and deployed on Hugging Face Spaces.

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python application.py
   ```

3. Open your browser and navigate to `http://localhost:8080`

## Docker Usage

1. Build the Docker image:
   ```bash
   docker build -t hotel-prediction .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 hotel-prediction
   ```

3. Access the application at `http://localhost:8080`