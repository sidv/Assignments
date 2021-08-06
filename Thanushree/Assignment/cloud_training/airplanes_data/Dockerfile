FROM ubuntu 

WORKDIR /home

COPY parseAirplanes.sh .

RUN chmod u+x parseAirplanes.sh
RUN apt-get update
RUN apt-get install -y wget
RUN wget https://corgis-edu.github.io/corgis/datasets/csv/airlines/airlines.csv


CMD [ "./parseAirplanes.sh" ]
