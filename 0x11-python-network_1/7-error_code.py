#!/usr/bin/python3
""""Python script that takes in a URL, sends a request to the URL
and displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    st_code = response.status_code
    if st_code < 400:
        print(st_code.text)
    else:
        print('Error code:', st_code)
