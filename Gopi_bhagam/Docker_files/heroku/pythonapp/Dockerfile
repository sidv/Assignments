#Choose Base image
#Import base Image
FROM python:3.9

#Set working directory
WORKDIR /app

#Set port
EXPOSE 4000

Copy server.py .
Copy requirements.txt .

#Install libraies
RUN pip install flask


CMD [ "python3", "server.py" ]

