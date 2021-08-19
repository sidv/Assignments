#Import image
FROM ubuntu

#set working directory
WORKDIR /home


#Copy files
COPY parseAirplanes.sh .


#install libraries
RUN apt-get update
RUN apt-get install -y wget
RUN wget https://corgis-edu.github.io/corgis/datasets/csv/airlines/airlines.csv 


#command
CMD ["./parseAirplanes.sh"]
