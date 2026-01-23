#1311. Get Watched Videos by Your Friends
#Medium
#
#There are n people, each person has a unique id between 0 and n-1. Given the
#arrays watchedVideos and friends, where watchedVideos[i] and friends[i]
#contain the list of watched videos and the list of friends respectively for
#the person with id = i.
#
#Level 1 of videos are all watched videos by your friends, level 2 of videos
#are all watched videos by the friends of your friends and so on. In general,
#the level k of videos are all watched videos by people with the shortest path
#exactly equal to k with you. Given your id and the level of videos, return
#the list of videos ordered by their frequencies (increasing). For videos with
#the same frequency order them alphabetically from least to greatest.
#
#Example 1:
#Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
#Output: ["B","C"]
#Explanation: You have id = 0 (green color) and your friends are (yellow):
#Person 1 watched "C". Person 2 watched "B" and "C".
#The frequencies of "B" and "C" are 1 and 2. Sorted by frequency: ["B","C"].
#
#Example 2:
#Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
#Output: ["D"]
#Explanation: You have id = 0 (green color) and the friends of your friends (orange):
#Person 3 watched "D".
#
#Constraints:
#    n == watchedVideos.length == friends.length
#    2 <= n <= 100
#    1 <= watchedVideos[i].length <= 100
#    1 <= watchedVideos[i][j].length <= 8
#    0 <= friends[i].length < n
#    0 <= friends[i][j] < n
#    0 <= id < n
#    1 <= level < n
#    if friends[i] contains j, then friends[j] contains i

from typing import List
from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int
    ) -> List[str]:
        """
        BFS to find friends at exactly 'level' distance.
        Then count their videos and sort.
        """
        # BFS to find friends at given level
        visited = {id}
        queue = deque([id])
        current_level = 0

        while queue and current_level < level:
            for _ in range(len(queue)):
                person = queue.popleft()
                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            current_level += 1

        # queue now contains friends at target level
        # Count their watched videos
        video_count = Counter()
        for person in queue:
            for video in watchedVideos[person]:
                video_count[video] += 1

        # Sort by frequency, then alphabetically
        videos = list(video_count.keys())
        videos.sort(key=lambda v: (video_count[v], v))

        return videos


class SolutionDetailed:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int
    ) -> List[str]:
        """More explicit BFS implementation"""
        n = len(friends)
        distances = [-1] * n
        distances[id] = 0

        queue = deque([id])

        while queue:
            person = queue.popleft()
            for friend in friends[person]:
                if distances[friend] == -1:
                    distances[friend] = distances[person] + 1
                    queue.append(friend)

        # Collect videos from people at target level
        video_count = Counter()
        for person in range(n):
            if distances[person] == level:
                for video in watchedVideos[person]:
                    video_count[video] += 1

        # Sort and return
        return sorted(video_count.keys(), key=lambda v: (video_count[v], v))
