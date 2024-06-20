#!/usr/bin/python3
"""1. Top Ten"""


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            d = get_data.get("data")
            t = d.get("title")
            print(t)
    else:
        print(None)
