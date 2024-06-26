#!/usr/bin/python3
"""This script displays the value of the X-Request-Id variable found in
the header of the response.

Usage: python3 7-error_code.py <URL>
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
