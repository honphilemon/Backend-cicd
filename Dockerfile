# Use an official Python runtime as a base image
FROM python:3.10-slim AS base

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Install any necessary Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Final stage
FROM python:3.10-slim

WORKDIR /app

COPY --from=base /app /app

# Command to run the Python script
CMD ["python", "service_binding.py"]
