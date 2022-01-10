#!/bin/bash
python3 ./getdata.py
python3 ./getdataeta.py
python3 ./comune.py "RENDE"
python3 ./comune.py "COSENZA"
python3 ./comune.py "MONTALTO UFFUGO"
python3 ./comune.py "BISIGNANO"
python3 eta.py
python3 ./weekly.py "RENDE" 35475
python3 ./weekly.py "COSENZA" 65563
python3 ./weekly.py "MONTALTO UFFUGO" 19930
python3 ./plot.py "RENDE" "COSENZA" "MONTALTO UFFUGO"