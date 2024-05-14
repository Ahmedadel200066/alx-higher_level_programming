#!/usr/bin/python3
"""This script displays the value of the X-Request-Id variable found in
the header of the response.

Usage: python3 5-hbtn_header.py <URL>
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    html = get(argv[1])
    print(html.headers.get('X-Request-Id'))
