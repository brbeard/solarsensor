#!/bin/bash

cd /home/pi/iotdash
source bin/activate
python3 Django-Chart.js/src/manage.py runserver

