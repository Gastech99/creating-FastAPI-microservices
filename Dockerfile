# Use the official Python image as the base image
FROM python:3.13-slim


# Set environment variables to prevent Python from writting .pyc files and to ensure stdout and stderr are flushed
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /redis

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /redis/

# Install the dependancies
#RUN Install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code into the container
COPY redis.py /redis//

# Expose the port on wich the app will run
EXPOSE 8000

# Command to run the FastAPI app using uvicorn
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000" ]