#Import image
FROM python:3.9

#set working directory
WORKDIR /app

#set port
EXPOSE 4000

#Copy files
COPY server.py .
COPY requirements.txt .

#install libraries
RUN pip install -r requirements.txt

#command
CMD ["python" , "server.py"]
