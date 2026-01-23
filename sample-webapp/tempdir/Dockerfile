FROM python:3.11-slim
RUN pip install --no-cache-dir --progress-bar off flask
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  sample-app.py /home/myapp/
WORKDIR /home/myapp
EXPOSE 8080
CMD python3 /home/myapp/sample-app.py
