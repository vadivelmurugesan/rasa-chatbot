# Base image with Rasa and SDK included
FROM rasa/rasa:3.6.21-full

# Switch to root to install packages
USER root

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the image
COPY . /app

# Install Python dependencies (if any custom ones)
RUN pip install --no-cache-dir -r requirements.txt

# Reset to Rasa's default user for security
USER 1001

# Expose Rasa port
EXPOSE 5005

# Run Rasa server, auto-loads latest model from /app/models
CMD ["run", "--enable-api", "--model", "/app/models", "--cors", "*", "--debug"]