#!/usr/bin/env sh
docker build . -t foodcourt
docker run  -p 5000:5000 foodcourt