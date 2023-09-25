#!/bin/bash
#Host port scanner script
echo "Enter the IP address/range :"
read IP
echo "Enter the port number :"
read port

nmap -sT $IP -p $port > /dev/null -oG result0
cat result0 | grep open > result1
cat result1
