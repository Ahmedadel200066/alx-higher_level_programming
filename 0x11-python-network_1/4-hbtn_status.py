#!/usr/bin/python3
"""This script displays the value of the X-Request-Id variable found in
the header of the response.

The script sends a GET request to 'https://alx-intranet.hbtn.io/status'
and prints the body response, including the type and content of the response.
"""

if __name__ == "__main__":
    from requests import get

    html = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
