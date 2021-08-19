#import image
FROM node:14

#set working directory
WORKDIR /app

#set port
EXPOSE 3000

#copy files
COPY app.js . 
COPY package.json .

#Install libraries
RUN npm install
#command
CMD [ "node", "app.js" ]
