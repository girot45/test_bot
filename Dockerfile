FROM python:3.9-slim

WORKDIR /test_bot

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "bot/main.py"]
