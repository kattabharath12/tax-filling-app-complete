FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt (it's now in the same directory as Dockerfile)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from current directory (backend/)
COPY . .

# Create uploads directory
RUN mkdir -p uploads

ENV PORT=8000
EXPOSE $PORT

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
