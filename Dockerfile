FROM python:3.11-slim

WORKDIR /test_bot

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
