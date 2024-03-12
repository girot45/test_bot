FROM python:3.9-slim

WORKDIR /test_bot

COPY . test_bot

RUN pip install -r requirements.txt

CMD ["python", "test_bot/bot/main.py"]
