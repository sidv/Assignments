FROM node:14

WORKDIR /usr/src/app

EXPOSE 3000

COPY app.js .
COPY package.json .

RUN npm install

cmd [ "node" , "app.js" ]


