FROM node:14


WORKDIR /app


EXPOSE 3000

COPY app.js .

COPY package.json .


RUN npm install


CMD ["node","app.js"]
