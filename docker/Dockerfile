FROM python:3.12-slim

WORKDIR /app

RUN pip install fastapi requests uvicorn

COPY ./app/main.py .

ENTRYPOINT ["python", "-m", "uvicorn", "--port", "9123", "--host", "0.0.0.0", "main:app"]
CMD ["--reload"]