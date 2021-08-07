FROM ubuntu

WORKDIR /home

RUN apt-get update
RUN apt-get install -y wget 
RUN wget https://corgis-edu.github.io/corgis/datasets/csv/airlines/airlines.csv 

COPY parseAirplanes.sh .
RUN chmod +x parseAirplanes.sh

CMD ["./parseAirplanes.sh"]
