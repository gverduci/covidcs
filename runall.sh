#!/bin/bash
python3 ./getdata.py
python3 ./getdataeta.py
python3 ./comune.py "RENDE"
python3 ./comune.py "BISIGNANO"
python3 ./comune.py "COSENZA"
python3 ./comune.py "MONTALTO UFFUGO"
python3 ./comune.py "CASTROVILLARI"
python3 eta.py