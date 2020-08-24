#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
with package requests"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    content = response.headers.get('X-Request-Id')
    print(content)
