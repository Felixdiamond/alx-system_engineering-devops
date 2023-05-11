import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
      subreddit: The name of the subreddit to query.

    Returns:
      None.
    """

    # Check if the subreddit is valid.
    if not subreddit:
        print("Please provide a valid subreddit name.")
        return

    # Make a request to the Reddit API.
    response = requests.get(
        "https://api.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        allow_redirects=False,
        headers={
            "User-Agent": "Ayanokoji/2.1"})

    # Check if the request was successful.
    if response.status_code != 200:
        print("Error: {} {}".format(response.status_code, response.reason))
        return

    # Parse the response data.
    data = response.json()

    # Print the titles of the first 10 hot posts.
    for post in data["data"]["children"]:
        print(post["data"]["title"])
