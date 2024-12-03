# syntax=docker/dockerfile:1
FROM python:3.10

# Create a directory named "/app" inside the Docker container
# The "-p" option ensures that parent directories are created if they don't exist
RUN mkdir -p /app
# Set the working directory inside the Docker container to "/app"
# This means that any subsequent commands will be executed relative to this directory
# It simplifies the path references in subsequent commands and makes the container's context clearer
WORKDIR /app

# Set Europe/Berlin timezone
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Copy the requirements file first to leverage Docker caching
COPY ../requirements.txt .

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY .. .

# Install dependencies
# These commands install the cv2 dependencies that are normally present on the local machine,
# but might be missing in your Docker container causing the issue.
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libmagic1 -y

# Define an argument named CONFIG_FILE with a default value of "5004"
# Arguments can be passed to Docker during the build process using the "--build-arg" flag
ENV UVICORN_PORT=5004

# Set the default command to be executed when the container starts
# It runs the "uvicorn" command with the arguments:
# - "main:app" specifies the module and the object to run (in this case, "main" module and "app" object)
# - "--host 0.0.0.0" specifies the host address to bind to (all available network interfaces)
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0"]
