#1683. Invalid Tweets
#Easy
#
#SQL Schema problem - implementing logic in Python
#
#Table: Tweets
#+----------------+---------+
#| Column Name    | Type    |
#+----------------+---------+
#| tweet_id       | int     |
#| content        | varchar |
#+----------------+---------+
#tweet_id is the primary key.
#content consists of English characters, digits, and ' '.
#
#Write a query to find the IDs of the invalid tweets. The tweet is invalid if
#the number of characters used in the content of the tweet is strictly greater
#than 15.

from typing import List, Dict

class Solution:
    def invalidTweets(self, tweets: List[Dict]) -> List[int]:
        """
        Filter tweets with content length > 15.
        """
        return [tweet['tweet_id'] for tweet in tweets
                if len(tweet['content']) > 15]


class SolutionExplicit:
    def invalidTweets(self, tweets: List[Dict]) -> List[int]:
        """
        Explicit loop implementation.
        """
        invalid = []

        for tweet in tweets:
            if len(tweet['content']) > 15:
                invalid.append(tweet['tweet_id'])

        return invalid


class SolutionSQL:
    """
    SQL equivalent:

    SELECT tweet_id
    FROM Tweets
    WHERE CHAR_LENGTH(content) > 15;

    -- Or using LENGTH (works for ASCII):
    -- SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15;
    """
    pass


class SolutionFilter:
    def invalidTweets(self, tweets: List[Dict]) -> List[int]:
        """
        Using filter function.
        """
        return list(map(
            lambda t: t['tweet_id'],
            filter(lambda t: len(t['content']) > 15, tweets)
        ))


class SolutionCompact:
    def invalidTweets(self, tweets: List[Dict]) -> List[int]:
        """
        Compact one-liner.
        """
        return [t['tweet_id'] for t in tweets if len(t['content']) > 15]
