#!/usr/bin/python3
"""2. Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """list containing the titles of all hot articles for a given subreddit"""
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            d = get_data.get("data")
            t = d.get("title")
            hot_list.append(t)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
