FROM python:3.12-slim

WORKDIR /app

# Copy the app folder and the config.yaml file
COPY src /app

# readme required by pip
COPY README.md /app
COPY pyproject.toml /app
COPY configs/config.yaml /app

# Install dependencies
RUN echo $(ls)
RUN pip install --no-cache-dir .[all]

EXPOSE 50052

# Use the environment variable in CMD
CMD ["sh", "-c", "allie-flowkit-python"]