FROM python:3.12.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY main.py .
COPY .env .

EXPOSE 5001

CMD ["python", "./main.py"]