#!/usr/bin/python3
"""
This script fetches the status of the URL 'https://alx-intranet.hbtn.io/status'
and prints the response body, its type, and the UTF-8 decoded content.
"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf-8 content: {}".format(content.decode('utf-8')))
