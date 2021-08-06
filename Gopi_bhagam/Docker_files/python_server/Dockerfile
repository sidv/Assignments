#IMPORT IMAGE
FROM python:3.9
#set working directory
WORKDIR /app

#set port
EXpose 4000

#copy files
copy server.py .
copy requirements.txt .

#install libraries
RUN pip install -r requirements.txt 

#command
CMD ["python "," server.py "]
