#import image
FROM python:3.9

#set working directory
WORKDIR /app

#set port
EXPOSE 4000

#copy files
COPY server.py .
copy requirements.txt .

#Install libraries
RUN pip install -r requirements.txt

#command
CMD [ "python", "server.py" ]
