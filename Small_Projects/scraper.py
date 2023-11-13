#!./env/bin/python3
import requests

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Check status code for response received
#success code - 2--
print(r)

# print content of request
print(r.content)
