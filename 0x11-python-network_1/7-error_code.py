#!/usr/bin/python3
""""Python script that takes in a URL, sends a request to the URL
and displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    try:
        query = requests.get(sys.argv[1])
        print(query.text)
    except HTTPError as error:
        print('Error code:', query.status_code)
