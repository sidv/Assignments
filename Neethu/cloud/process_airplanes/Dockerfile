FROM ubuntu

WORKDIR /home

COPY parseAirplanes.sh .

RUN apt-get update

RUN apt-get install -y  wget

RUN wget https://corgis-edu.github.io/corgis/datasets/csv/airlines/airlines.csv

RUN chmod +x parseAirplanes.sh


CMD ["./parseAirplanes.sh"]
