FROM ubuntu

WORKDIR /usr/src/app

COPY parseAirplanes.sh .

RUN chmod +x parseAirplanes.sh
RUN apt-get update
RUN apt-get install -y wget
RUN wget https://corgis-edu.github.io/corgis/datasets/csv/airlines/airlines.csv

CMD [ "./parseAirplanes.sh" ]
