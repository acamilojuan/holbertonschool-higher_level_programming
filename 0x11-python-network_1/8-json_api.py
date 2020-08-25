#!/usr/bin/python3
""""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('No result')
    else:
        try:
            url = 'http://0.0.0.0:5000/search_user'
            response = requests.post(url, data={'q': sys.argv[1]}).json()
            if response:
                print("[{}] {}".format(response.get('id'),
                      response.get('name')))
            else:
                print('No result')
        except Exception:
            print('Not a valid JSON')
