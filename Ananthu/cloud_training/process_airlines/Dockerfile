FROM ubuntu

WORKDIR /usr/src/app

COPY parseAirplanes.sh .

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://corgis-edu.github.io/corgis/datasets/csv/airlines/airlines.csv
RUN chmod u+x parseAirplanes.sh

CMD ["./parseAirplanes.sh"]
