FROM python:latest
WORKDIR /opt/ass-app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ass-app
EXPOSE 5001
ENTRYPOINT ["/usr/local/bin/python", "ass-app/app.py"]
