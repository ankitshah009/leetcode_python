#1947. Maximum Compatibility Score Sum
#Medium
#
#There is a survey that consists of n questions where each question's answer is
#either 0 (no) or 1 (yes).
#
#The survey was given to m students numbered from 0 to m - 1 and m mentors
#numbered from 0 to m - 1. The answers of the students are represented by a 2D
#integer array students where students[i] is an integer array that contains the
#answers of the ith student (0-indexed). The answers of the mentors are
#represented by a 2D integer array mentors where mentors[j] is an integer array
#that contains the answers of the jth mentor (0-indexed).
#
#The compatibility score of a student and a mentor is the number of answers
#that are the same for both the student and the mentor.
#
#You are tasked with finding the optimal student-mentor pairings to maximize
#the sum of the compatibility scores.
#
#Given students and mentors, return the maximum compatibility score sum that
#can be achieved.
#
#Example 1:
#Input: students = [[1,1,0],[1,0,1],[0,0,1]],
#       mentors = [[1,0,0],[0,0,1],[1,1,0]]
#Output: 8
#
#Example 2:
#Input: students = [[0,0],[0,0],[0,0]],
#       mentors = [[1,1],[1,1],[1,1]]
#Output: 0
#
#Constraints:
#    m == students.length == mentors.length
#    n == students[i].length == mentors[j].length
#    1 <= m, n <= 8
#    students[i][k] is either 0 or 1.
#    mentors[j][k] is either 0 or 1.

from typing import List
from functools import lru_cache

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """
        Bitmask DP for assignment problem.
        """
        m = len(students)

        # Precompute compatibility scores
        scores = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                scores[i][j] = sum(s == t for s, t in zip(students[i], mentors[j]))

        @lru_cache(maxsize=None)
        def dp(student: int, mentor_mask: int) -> int:
            if student == m:
                return 0

            max_score = 0
            for mentor in range(m):
                if not (mentor_mask & (1 << mentor)):
                    score = scores[student][mentor] + dp(student + 1, mentor_mask | (1 << mentor))
                    max_score = max(max_score, score)

            return max_score

        return dp(0, 0)


class SolutionPermutation:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """
        Try all permutations of mentor assignments.
        """
        from itertools import permutations

        m = len(students)
        n = len(students[0])

        def score(s, t):
            return sum(a == b for a, b in zip(s, t))

        max_total = 0

        for perm in permutations(range(m)):
            total = sum(score(students[i], mentors[perm[i]]) for i in range(m))
            max_total = max(max_total, total)

        return max_total


class SolutionIterative:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """
        Iterative bitmask DP.
        """
        m = len(students)

        # Precompute scores
        scores = [[sum(s == t for s, t in zip(students[i], mentors[j]))
                   for j in range(m)] for i in range(m)]

        # dp[mask] = max score using mentors in mask
        dp = [0] * (1 << m)

        for mask in range(1 << m):
            student = bin(mask).count('1')
            if student >= m:
                continue

            for mentor in range(m):
                if not (mask & (1 << mentor)):
                    new_mask = mask | (1 << mentor)
                    dp[new_mask] = max(dp[new_mask], dp[mask] + scores[student][mentor])

        return dp[(1 << m) - 1]
