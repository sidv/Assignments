FROM python:3.9

WORKDIR /usr/src/app

EXPOSE 4000

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY server.py .

CMD ["python3","server.py"]

