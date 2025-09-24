FROM python:3.11-slim

WORKDIR /app

COPY . /app

COPY images/titanic.png /app/images/titanic.png

# Install dependencies
RUN pip install --no-cache-dir requests flet

EXPOSE 8550

# Launch the application
CMD ["python", "app.py"]
