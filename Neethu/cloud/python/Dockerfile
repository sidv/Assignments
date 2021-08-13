FROM python:3.9

WORKDIR /usr/src/app

EXPOSE 4000

COPY server.py .
COPY requirements.txt .

RUN pip install -r  requirements.txt




CMD ["python","server.py"]
