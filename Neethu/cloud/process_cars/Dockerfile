#Import image

FROM Ubuntu

WORKDIR /home

RUN apt-get update
RUN apt-get install wget

RUN wget 

COPY cars_filter.sh .

COPY cars.csv .

CMD ["./cars_filter.sh" ]





