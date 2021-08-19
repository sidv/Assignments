#import image
FROM httpd

#set working directory
WORKDIR /usr/local/apache2/htdocs/
#set port
EXPOSE 80

COPY index.html /usr/local/apache2/htdocs/
COPY register.html /usr/local/apache2/htdocs/
COPY signup.html /usr/local/apache2/htdocs/

RUN mkdir data
