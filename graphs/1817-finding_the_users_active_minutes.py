#1817. Finding the Users Active Minutes
#Medium
#
#You are given the logs for users' actions on LeetCode, and an integer k. The
#logs are represented by a 2D integer array logs where each logs[i] = [ID_i,
#time_i] indicates that the user with ID_i performed an action at the minute
#time_i.
#
#Multiple users can perform actions simultaneously, and a single user can
#perform multiple actions in the same minute.
#
#The user active minutes (UAM) for a given user is defined as the number of
#unique minutes in which the user performed an action on LeetCode. A minute can
#only be counted once, even if multiple actions occur during it.
#
#You are to calculate a 1-indexed array answer of size k such that, for each j
#(1 <= j <= k), answer[j] is the number of users whose UAM equals j.
#
#Return the array answer as described above.
#
#Example 1:
#Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
#Output: [0,2,0,0,0]
#
#Example 2:
#Input: logs = [[1,1],[2,2],[2,3]], k = 4
#Output: [1,1,0,0]
#
#Constraints:
#    1 <= logs.length <= 10^4
#    0 <= ID_i <= 10^9
#    1 <= time_i <= 10^5
#    k is in the range [The maximum UAM for a user, 10^5].

from typing import List
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        """
        Group unique minutes per user, then count UAM frequencies.
        """
        user_minutes = defaultdict(set)

        for user_id, time in logs:
            user_minutes[user_id].add(time)

        answer = [0] * k

        for minutes in user_minutes.values():
            uam = len(minutes)
            if uam <= k:
                answer[uam - 1] += 1

        return answer


class SolutionCounter:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        """
        Using Counter for UAM frequency.
        """
        from collections import Counter

        user_minutes = defaultdict(set)
        for uid, time in logs:
            user_minutes[uid].add(time)

        uam_counts = Counter(len(m) for m in user_minutes.values())

        return [uam_counts.get(j, 0) for j in range(1, k + 1)]
