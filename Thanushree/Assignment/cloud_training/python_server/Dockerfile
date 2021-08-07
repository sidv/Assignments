#choose base image
#import base image

FROM python:3.9

#set working directory
WORKDIR /usr/src/app

#set port
EXPOSE 4000


#copy required file
COPY server.py .
COPY requirements.txt .

#install libraries
RUN pip install -r requirements.txt


#passing the commands
CMD [ "python3" , "server.py" ]
