# Используем официальный образ Python
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn pandas scikit-learn pydantic

EXPOSE 8000

# Launch 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
