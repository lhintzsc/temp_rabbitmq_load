#!/bin/bash

while [ 1 -eq 1 ]; do
  #echo "next interval"  
  timeout 1 ./receive.py
  sleep 5
done
