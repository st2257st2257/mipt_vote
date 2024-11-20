FROM python:3.10-slim

COPY . .
RUN pip install -r requirements.txt
RUN pip install fastapi-admin

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
