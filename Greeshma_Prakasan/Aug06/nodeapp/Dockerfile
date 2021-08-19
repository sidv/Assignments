FROM node:14

WORKDIR /usr/src/app

COPY package.json .

RUN apt-get update
RUN npm install 

COPY app.js .

CMD ["node","app.js"]
