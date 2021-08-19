FROM node:14
WORKDIR /home
EXPOSE 3000
COPY app.js .
COPY package.json .
RUN apt-get update
RUN npm install
CMD [ "node", "app.js"]
