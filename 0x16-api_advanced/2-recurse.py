#!/usr/bin/python3

"""
    Queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit.

    Args:
      subreddit: The name of the subreddit to query.
      hot_list: A list to store the titles of the hot articles.

    Returns:
      A list containing the titles of the hot articles.
    """
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """returns a list containing the titles
    of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Ayanokoji/2.1"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
