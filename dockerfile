
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
EXPOSE 8081
CMD ["uvicorn","app.py"]

