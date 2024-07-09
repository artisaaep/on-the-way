# Stage 1: Base stage with Python dependencies
FROM python:3.11-slim as python-base

WORKDIR /on-the-way

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 2: Final stage with Nginx and Python
FROM harbor.pg.innopolis.university/docker-hub-cache/debian:11-slim

# Install Nginx
RUN apt update && apt install --no-install-recommends -y nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && sudo apt-get update && sudo apt-get upgrade libdb5.3 && sudo apt-get upgrade zlib1g

# Copy built Python environment and application code
COPY --from=python-base /on-the-way /on-the-way

# Configure Nginx (assuming you have an nginx.conf file)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port your application runs on
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Command to run Nginx and Python applications
CMD ["sh", "-c", "nginx & python /on-the-way/main.py & python /on-the-way/server_main.py"]
