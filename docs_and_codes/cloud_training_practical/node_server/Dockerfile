#Import image
FROM node:14

#SET working directory
WORKDIR /app

#EXPOSE
EXPOSE 3000

#COpy source code
COPY src/ .

#INSTALL libraries
RUN npm install


#Launch app
CMD ["node" , "app.js"]
