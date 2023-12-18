# Use a specific version of Alpine Linux as the base image
FROM alpine:3.15.3

# Update packages and install necessary tools
RUN apk update && apk upgrade && \
    apk add --no-cache python3~=3.9 py3-pip build-base libffi-dev musl-dev python3-dev cmake

# Set the working directory in the container
WORKDIR /app

# Install specific versions of Python packages without using a requirements.txt file
RUN pip install --no-cache-dir \
    fastapi==0.104.1 \
    numpy==1.26.2 \
    uvicorn==0.15.0 \
    pandas==1.3.3 \
    plotly==5.3.1

# Copy the rest of the files into the container
COPY . .

# Expose the port that the FastAPI app will run on
EXPOSE 5000

# Command to run the FastAPI app using uvicorn
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
