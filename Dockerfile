FROM python:3.7.3-slim
LABEL version="0.1.0"
ADD . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","app.py"]
