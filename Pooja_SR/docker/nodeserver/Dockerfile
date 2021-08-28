FROM node:14

WORKDIR /home

EXPOSE 4000

COPY app.js .
COPY package.json .

RUN npm install 

CMD [ "node", "app.js" ]
