#IMPORT image
From node:14

#set working directory
WORKDIR /app

#EXPOse
EXPOSE 3000

#copy source code

COPY app.js .
COPY package.json .
#install libraries
RUN npm install

#Launch app
CMD [“node” ,“app.js”]
