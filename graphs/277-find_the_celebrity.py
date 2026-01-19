#277. Find the Celebrity
#Medium
#
#Suppose you are at a party with n people labeled from 0 to n - 1 and among them,
#there may exist one celebrity. The definition of a celebrity is that all the
#other n - 1 people know the celebrity, but the celebrity does not know any of them.
#
#Now you want to find out who the celebrity is or verify that there is not one.
#You are only allowed to ask questions like: "Hi, A. Do you know B?" to get
#information about whether A knows B. You need to find out the celebrity (or verify
#there is not one) by asking as few questions as possible (in the asymptotic sense).
#
#You are given a helper function bool knows(a, b) that tells you whether a knows b.
#Implement a function int findCelebrity(n). There will be exactly one celebrity
#if they are at the party.
#
#Return the celebrity's label if there is a celebrity at the party. If there is
#no celebrity, return -1.
#
#Example 1:
#Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
#Output: 1
#Explanation: Person 0 knows person 1. Person 2 knows persons 0 and 1. Person 1
#knows nobody. Hence person 1 is the celebrity.
#
#Example 2:
#Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
#Output: -1
#
#Constraints:
#    n == graph.length == graph[i].length
#    2 <= n <= 100
#    graph[i][j] is 0 or 1
#    graph[i][i] == 1
#
#Follow up: If the maximum number of allowed calls to the API knows is 3 * n,
#could you find a solution without exceeding the maximum number of calls?

# The knows API is already defined for you.
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Find potential celebrity candidate
        candidate = 0

        for i in range(1, n):
            if knows(candidate, i):
                # candidate knows i, so candidate is not celebrity
                # i could be celebrity
                candidate = i

        # Verify candidate is actually celebrity
        for i in range(n):
            if i == candidate:
                continue
            # Celebrity should not know anyone, and everyone should know celebrity
            if knows(candidate, i) or not knows(i, candidate):
                return -1

        return candidate

    # Alternative with caching
    def findCelebrityWithCache(self, n: int) -> int:
        cache = {}

        def cached_knows(a, b):
            if (a, b) not in cache:
                cache[(a, b)] = knows(a, b)
            return cache[(a, b)]

        candidate = 0
        for i in range(1, n):
            if cached_knows(candidate, i):
                candidate = i

        for i in range(n):
            if i == candidate:
                continue
            if cached_knows(candidate, i) or not cached_knows(i, candidate):
                return -1

        return candidate
