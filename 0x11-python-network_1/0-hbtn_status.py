#!/usr/bin/python3

import urllib.request

def fetch_status(url):
    """
    Fetches the HTTP status code, content type, and response content from a given URL.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None

    Prints:
        HTTP Status Code: The HTTP status code of the response.
        Content-Type: The content type of the response.
        Response Content: The content of the response.
    """
    try:
        # Open the URL
        with urllib.request.urlopen(url) as response:
            # Read the content of the response
            content = response.read()
            # Get the HTTP status code
            status_code = response.status
            # Get the content type header
            content_type = response.getheader('Content-Type')

            # Print out the results
            print("HTTP Status Code:", status_code)
            print("Content-Type:", content_type)
            print("Response Content:", content)
    except urllib.error.URLError as e:
        print("Failed to reach the server.")
        print("Reason:", e.reason)
    except urllib.error.HTTPError as e:
        print("The server couldn't fulfill the request.")
        print("Error code:", e.code)
    except Exception as e:
        print("An error occurred:", str(e))
