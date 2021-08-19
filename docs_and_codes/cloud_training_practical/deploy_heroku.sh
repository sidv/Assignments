#!/bin/bash

heroku container:login
heroku container:push web  --app $1
heroku container:release web --app $1
heroku open --app $1
