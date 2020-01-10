FROM python:latest
WORKDIR /opt/ff-server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ass-app
EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/python", "ass-app/app.py"]
