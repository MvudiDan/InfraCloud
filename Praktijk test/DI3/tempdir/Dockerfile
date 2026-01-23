FROM python:3.10-slim
RUN pip install --no-cache-dir --progress-bar off flask
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD python3 app.py
