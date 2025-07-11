FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy from the build context (which includes the backend folder)
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

# Create uploads directory
RUN mkdir -p uploads

# Set default port
ENV PORT=8000
EXPOSE $PORT

# Use a startup script
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
