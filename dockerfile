
FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi uvicorn[standard]
COPY app.py .
EXPOSE 8081
CMD ["uvicorn","app.py"]

