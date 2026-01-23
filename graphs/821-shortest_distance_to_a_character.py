#821. Shortest Distance to a Character
#Easy
#
#Given a string s and a character c that occurs in s, return an array of
#integers answer where answer.length == s.length and answer[i] is the distance
#from index i to the closest occurrence of character c in s.
#
#The distance between two indices i and j is abs(i - j).
#
#Example 1:
#Input: s = "loveleetcode", c = "e"
#Output: [3,2,1,0,1,0,0,1,2,2,1,0]
#
#Example 2:
#Input: s = "aaab", c = "b"
#Output: [3,2,1,0]
#
#Constraints:
#    1 <= s.length <= 10^4
#    s[i] and c are lowercase English letters.
#    It is guaranteed that c occurs at least once in s.

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        """
        Two passes: left-to-right and right-to-left.
        """
        n = len(s)
        result = [float('inf')] * n

        # Left to right: distance from previous c
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev

        # Right to left: distance from next c
        next_c = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_c = i
            result[i] = min(result[i], next_c - i)

        return result


class SolutionPositions:
    """Store positions and use binary search"""

    def shortestToChar(self, s: str, c: str) -> list[int]:
        from bisect import bisect_left

        positions = [i for i, ch in enumerate(s) if ch == c]
        result = []

        for i in range(len(s)):
            idx = bisect_left(positions, i)
            left_dist = i - positions[idx - 1] if idx > 0 else float('inf')
            right_dist = positions[idx] - i if idx < len(positions) else float('inf')
            result.append(min(left_dist, right_dist))

        return result


class SolutionBFS:
    """BFS from all c positions"""

    def shortestToChar(self, s: str, c: str) -> list[int]:
        from collections import deque

        n = len(s)
        result = [-1] * n
        queue = deque()

        for i, ch in enumerate(s):
            if ch == c:
                queue.append(i)
                result[i] = 0

        while queue:
            i = queue.popleft()
            for j in [i - 1, i + 1]:
                if 0 <= j < n and result[j] == -1:
                    result[j] = result[i] + 1
                    queue.append(j)

        return result
