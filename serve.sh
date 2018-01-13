#!/bin/sh
ts=$(date)
printf "\n$ts : started server\n" >> log
python app.py >> log 2>&1
ts=$(date)
printf "\n$ts : server exited\n" >> log
