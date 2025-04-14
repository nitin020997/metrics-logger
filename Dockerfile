FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install psutil
CMD ["python", "app.py"]