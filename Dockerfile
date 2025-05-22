# Use official python image
FROM python:3.10-slim

# Set environment variables
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install Dependecies
COPY requirement.txt /app

RUN pip install --upgrade pip && pip install -r requirement.txt

# Copy project files
COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]