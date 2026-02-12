
FROM python:3.11-slim
WORKDIR /app
COPY sample.py .
EXPOSE 8081
CMD ["python", "sample.py"]

