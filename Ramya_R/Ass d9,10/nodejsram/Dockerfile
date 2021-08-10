#Choose Base image
#Import base Image
FROM node:14

#Set working directory
WORKDIR /app

#Set port
EXPOSE 3000

#Install libraies
COPY app.js .
COPY package.json .

RUN npm install

CMD [ "node", "app.js" ]
