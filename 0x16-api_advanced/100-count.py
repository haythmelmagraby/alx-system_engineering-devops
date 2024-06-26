#!/usr/bin/python3
"""3. Count it!"""
import requests


def count_words(subreddit, word_list, word_count=[], page_after=None):
    """parses the title of all hot articles, and prints a sorted count"""
    client_agent = {'User-Agent': 'HolbertonSchool'}
    word_list = [word.lower() for word in word_list]
    if bool(word_count) is False:
        for word in word_list:
            word_count.append(0)

    if page_after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        req = requests.get(url, headers=client_agent, allow_redirects=False)
        if req.status_code == 200:
            for child in req.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1

            if req.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, req.json()['data']['after'])
    else:
        url = ('https://www.reddit.com/r/{}/hot.json?after={}'
               .format(subreddit,
                       page_after))
        req = requests.get(url, headers=client_agent, allow_redirects=False)

        if req.status_code == 200:
            for child in req.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [wor for wor
                                 in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1
            if req.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, req.json()['data']['after'])
            else:
                dic_to = {}
                for key_word in list(set(word_list)):
                    i = word_list.index(key_word)
                    if word_count[i] != 0:
                        dic_to[word_list[i]] = (word_count[i] *
                                                word_list.count(word_list[i]))
                for key, value in sorted(dic_to.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(key, value))
