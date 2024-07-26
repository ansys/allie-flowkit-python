FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Set default number of workers
ENV WORKERS=4

# Use the environment variable in CMD
CMD ["sh", "-c", "uvicorn app.app:app --host 0.0.0.0 --port 8000 --workers ${WORKERS}"]

