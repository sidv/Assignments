#importing base image
FROM python:3.9
#adding work directory
WORKDIR /home

EXPOSE 4000

COPY server.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "./server.py"]
