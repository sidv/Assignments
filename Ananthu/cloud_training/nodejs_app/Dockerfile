FROM node:14

WORKDIR /usr/src/app

COPY app.js .
COPY package.json .

EXPOSE 3000

RUN npm install

CMD ["node","app.js"]
