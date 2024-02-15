#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit"""

    params = {}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    if after:
        params['after'] = after
    res = requests.get(url, params=params, headers=headers,
                       allow_redirects=False)

    if response.status_code != 200:
        return None
    results = response.json()
    for post in res['data']['children']:
        hot_list.append(post['data']['title'])

    if res['data']['after'] is None:
        return hot_list

    after = res['data']['after']

    return recurse(subreddit, hot_list, after)
