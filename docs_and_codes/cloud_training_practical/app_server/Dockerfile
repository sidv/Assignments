#Choose Base image
#Import base Image
FROM python:3.9

#Set working directory
WORKDIR /app

#Set port
EXPOSE 5000

#Install libraies
RUN pip install flask

COPY app/server.py .

CMD [ "python3", "server.py" ]

