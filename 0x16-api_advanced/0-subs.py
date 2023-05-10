#!/usr/bin/python3

"""
number_of_subscribers(subreddit)

Returns the number of subscribers for a given subreddit.

Args:
  subreddit (str): The name of the subreddit.

Returns:
  int: The number of subscribers.

Raises:
  ValueError: If the subreddit is not valid.
"""

from fake_useragent import UserAgent
import requests


def number_of_subscribers(subreddit):
    # Check if the subreddit is valid.
    if not subreddit.startswith("r/"):
        raise ValueError("The subreddit must start with 'r/'.")

    # Make a request to the Reddit API.
    response = requests.get(
        'https://api.reddit.com/r/{}/about.json'.format(subreddit),
        allow_redirects=False,
        headers={
            "User-Agent": UserAgent().random
        }
    )

    # Check the response status code.
    if response.status_code == 200:
        # Decode the JSON response.
        data = response.json()

        # Return the number of subscribers.
        return data["data"]["subscribers"]
    else:
        # Return 0 if the request failed.
        return 0
