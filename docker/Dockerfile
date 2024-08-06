FROM python:3.12-slim

WORKDIR /app

# Copy the app folder and the config.yaml file
COPY requirements.txt .
COPY app/ ./src/allie/flowkit/
COPY configs/config.yaml .

# Install dependencies
RUN pip install --no-cache-dir .

EXPOSE 8000

# Set default number of workers
ENV WORKERS=4

# Use the environment variable in CMD
CMD ["sh", "-c", "allie-flowkit --host 0.0.0.0 --port 8000 --workers $WORKERS"]