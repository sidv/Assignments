#Import image

FROM ubuntu

WORKDIR /home

RUN apt-get update
RUN apt-get install wget
RUN wget https://corgis-edu.github.io/corgis/datasets/csv/airlines/airlines.csv

COPY parseAirplanes.sh .

CMD ["./parseAirplanes.sh"]
