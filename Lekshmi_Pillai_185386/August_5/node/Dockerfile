#Import image
FROM node:14

#set working directory
WORKDIR /app

#set port
EXPOSE 3000

#Copy files
COPY app.js .
COPY package.json .

#install libraries
RUN npm install

#command
CMD ["node" , "app.js"]
