#!/usr/bin/python3
"""2. Recurse it!"""


def recurse(subreddit, hot_list=[], after='', count=0):
    """list containing the titles of all hot articles for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    the_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client_agent = {'User-agent': 'haythm ubuntu 20.2'}
    parameters = {
            'limit': 10,
            'count': count,
            'after': after
            }
    res = requests.get(the_url, headers=client_agent, params=parameters,
                       allow_redirects=False)

    if res.status_code == 404:
        print("None")
        return

    try:
        result = res.json().get('data')
        after = result.get('after')
        count += result.get('dist')
        [hot_list.append(child.get('data').get('title'))
         for child in result.get('children')]

        if after is not None:
            return recuse(subreddit, hot_list, after, count)

    except Exception:
        return 0
