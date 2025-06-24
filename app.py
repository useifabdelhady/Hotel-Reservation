# This file is for Hugging Face Spaces compatibility
# It simply imports and runs the Flask application

from application import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)  # Hugging Face Spaces uses port 7860 by default