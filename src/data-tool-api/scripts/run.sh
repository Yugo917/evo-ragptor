#!/bin/bash
# #########################
# Run application
# #########################

# Ensure dependencies are installed
poetry install

# Run FastAPI app using Uvicorn from the correct module
poetry run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload