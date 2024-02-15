#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, after=None, hot_list=[]):
    """a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit"""

    if subreddit:
        params = {}
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        headers = {'User-Agent': 'Mozilla/5.0'}

        if after:
            params['after'] = after
        res = requests.get(url, params=params, headers=headers).json()

        if 'data' in res and 'children' in res['data']:
            if len(res['data']['children']) > 0:
                for post in res['data']['children']:
                    hot_list.append(post['data']['title'])

                after = res['data']['after']

                if after is None:
                    return hot_list

                return recurse(subreddit, after, hot_list)

                return hot_list
            else:
                return None
    else:
        return None
