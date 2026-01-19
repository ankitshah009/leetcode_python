#355. Design Twitter
#Medium
#
#Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
#and is able to see the 10 most recent tweets in the user's news feed.
#
#Implement the Twitter class:
#    Twitter() Initializes your twitter object.
#    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
#    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
#    void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
#    void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
#
#Example 1:
#Input: ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
#       [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
#Output: [null, null, [5], null, null, [6, 5], null, [5]]
#
#Constraints:
#    1 <= userId, followerId, followeeId <= 500
#    0 <= tweetId <= 10^4
#    All the tweets have unique IDs.

from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # userId -> [(time, tweetId), ...]
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get all users whose tweets we need to consider
        users = self.following[userId] | {userId}

        # Use heap to get 10 most recent
        heap = []
        for user in users:
            for tweet in self.tweets[user]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)

        # Return in reverse chronological order
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
