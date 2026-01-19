#355. Design Twitter
#Medium
#
#Design a simplified version of Twitter where users can post tweets,
#follow/unfollow another user, and is able to see the 10 most recent tweets in
#the user's news feed.
#
#Implement the Twitter class:
#- Twitter() Initializes your twitter object.
#- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId
#  by the user userId. Each call to this function will be made with a unique
#  tweetId.
#- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs
#  in the user's news feed. Each item in the news feed must be posted by users
#  who the user followed or by the user themself. Tweets must be ordered from
#  most recent to least recent.
#- void follow(int followerId, int followeeId) The user with ID followerId
#  started following the user with ID followeeId.
#- void unfollow(int followerId, int followeeId) The user with ID followerId
#  started unfollowing the user with ID followeeId.
#
#Example:
#Input: ["Twitter", "postTweet", "getNewsFeed", "follow", "getNewsFeed",
#        "unfollow", "getNewsFeed"]
#       [[], [1, 5], [1], [1, 2], [1], [1, 2], [1]]
#Output: [null, null, [5], null, [5, 6], null, [5]]
#
#Constraints:
#    1 <= userId, followerId, followeeId <= 500
#    0 <= tweetId <= 10^4
#    All the tweets have unique IDs.
#    At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and
#    unfollow.

from typing import List
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.timestamp = 0
        # userId -> [(timestamp, tweetId), ...]
        self.tweets = defaultdict(list)
        # userId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get all users whose tweets should appear in feed
        users = self.following[userId] | {userId}

        # Merge k sorted lists using heap
        # Heap: (-timestamp, tweetId, userId, tweetIndex)
        heap = []

        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                ts, tweet_id = self.tweets[user][idx]
                heapq.heappush(heap, (-ts, tweet_id, user, idx))

        result = []

        while heap and len(result) < 10:
            neg_ts, tweet_id, user, idx = heapq.heappop(heap)
            result.append(tweet_id)

            if idx > 0:
                ts, next_tweet_id = self.tweets[user][idx - 1]
                heapq.heappush(heap, (-ts, next_tweet_id, user, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


class TwitterSimple:
    """Simpler implementation without heap optimization"""

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}

        # Collect all tweets from relevant users
        all_tweets = []
        for user in users:
            all_tweets.extend(self.tweets[user])

        # Sort by timestamp descending and take top 10
        all_tweets.sort(reverse=True)
        return [tweet_id for _, tweet_id in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
