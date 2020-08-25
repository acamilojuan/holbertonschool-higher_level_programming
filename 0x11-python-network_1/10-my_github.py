#!/usr/bin/python3
""""Python script that takes Github credentials
(username and password) and uses the Github API to display the user id"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://api.github.com/user', auth=(sys.argv[1],
                            sys.argv[2])).json().get('id')
    print(response)
