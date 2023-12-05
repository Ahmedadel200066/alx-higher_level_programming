#!/usr/bin/python3
"""This script displays the value of the X-Request-Id variable found in
the header of the response.

Usage: python3 0-hbtn_status.py <URL>
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
