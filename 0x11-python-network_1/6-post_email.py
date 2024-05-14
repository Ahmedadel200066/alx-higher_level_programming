#!/usr/bin/python3
"""This script sends a POST request to a specified URL with an email parameter.

The script takes two command-line arguments: the URL to send the request to and the email parameter value.
It uses the `requests` library to send the POST request and prints the response text.

Example usage:
    $ python3 6-post_email.py http://example.com/submit_email example@example.com
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    html = post(argv[1], data={'email': argv[2]})
    print(html.text)
