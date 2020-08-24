#!/usr/bin/python3
""""Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8)."""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
