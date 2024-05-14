#!/bin/bash

# Check if the virtual environment directory exists
if [ ! -d "venv" ]; then
  # Create a virtual environment
  python3 -m venv venv
  echo "Virtual environment created."
fi

# Activate the virtual environment
source venv/bin/activate
echo "Virtual environment activated."

# Check if Flask is installed
if ! python3 -c "import flask" &> /dev/null; then
  # Install Flask
  pip3 install Flask
  echo "Flask installed."
else
  echo "Flask is already installed."
fi

# Run the Flask application
python3 app.py