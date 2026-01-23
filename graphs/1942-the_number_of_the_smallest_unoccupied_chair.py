#1942. The Number of the Smallest Unoccupied Chair
#Medium
#
#There is a party where n friends numbered from 0 to n - 1 are attending. There
#is an infinite number of chairs in this party that are numbered from 0 to
#infinity. When a friend arrives at the party, they sit on the unoccupied chair
#with the smallest number.
#
#When a friend leaves the party, their chair becomes unoccupied at the moment
#they leave. If another friend arrives at that same moment, they can sit in
#that chair.
#
#You are given a 0-indexed 2D integer array times where times[i] = [arrival_i,
#leaving_i], indicating the arrival and leaving times of the ith friend
#respectively.
#
#Return the chair number that the friend numbered targetFriend will sit on.
#
#Example 1:
#Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
#Output: 1
#
#Example 2:
#Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
#Output: 2
#
#Constraints:
#    n == times.length
#    2 <= n <= 10^4
#    1 <= arrival_i < leaving_i <= 10^5
#    0 <= targetFriend <= n - 1
#    Each arrival_i time is distinct.

from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        """
        Simulate with two heaps: available chairs and leaving times.
        """
        n = len(times)
        target_arrival = times[targetFriend][0]

        # Sort friends by arrival time
        friends = sorted(range(n), key=lambda i: times[i][0])

        # Min-heap of available chairs
        available = list(range(n))
        heapq.heapify(available)

        # Min-heap of (leaving_time, chair) for occupied chairs
        leaving = []

        for friend in friends:
            arrival, leave = times[friend]

            # Free up chairs for friends who have left
            while leaving and leaving[0][0] <= arrival:
                _, chair = heapq.heappop(leaving)
                heapq.heappush(available, chair)

            # Assign smallest available chair
            chair = heapq.heappop(available)

            if friend == targetFriend:
                return chair

            heapq.heappush(leaving, (leave, chair))

        return -1  # Should not reach


class SolutionDetailed:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        """
        Same approach with clearer structure.
        """
        events = []

        for i, (arrive, leave) in enumerate(times):
            events.append((arrive, 0, i))  # Arrival event
            events.append((leave, 1, i))   # Leaving event

        events.sort()

        available = list(range(len(times)))
        heapq.heapify(available)

        chairs = {}  # friend -> chair

        for time, event_type, friend in events:
            if event_type == 1:  # Leaving
                heapq.heappush(available, chairs[friend])
            else:  # Arriving
                chair = heapq.heappop(available)
                chairs[friend] = chair

                if friend == targetFriend:
                    return chair

        return -1
