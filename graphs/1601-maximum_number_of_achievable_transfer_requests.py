#1601. Maximum Number of Achievable Transfer Requests
#Hard
#
#We have n buildings numbered from 0 to n - 1. Each building has a number of
#employees. It's transfer season, and some employees want to change the building
#they reside in.
#
#You are given an array requests where requests[i] = [fromi, toi] represents
#an employee's request to transfer from building fromi to building toi.
#
#All buildings are full, so a list of requests is achievable only if for each
#building, the net change in employee transfers is zero. This means the number
#of employees leaving is equal to the number of employees moving in. For example,
#if n = 3 and two employees are leaving building 0, one is leaving building 1,
#and one is leaving building 2, there should be two employees moving to building 0,
#one employee moving to building 1, and one employee moving to building 2.
#
#Return the maximum number of achievable requests.
#
#Example 1:
#Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
#Output: 5
#Explanation: Let's see the requests:
#From building 0 we have employees x and y and both want to move to building 1.
#From building 1 we have employees a and b and they want to move to buildings 0
#and 2 respectively.
#From building 2 we have employee z and they want to move to building 0.
#From building 3 we have employee c and they want to move to building 4.
#From building 4 we have no requests.
#We can achieve the requests of users x and b by swapping their places.
#We can achieve the requests of users y, a and z by swapping the places in the
#3 buildings.
#
#Example 2:
#Input: n = 3, requests = [[0,0],[1,2],[2,1]]
#Output: 3
#
#Example 3:
#Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
#Output: 4
#
#Constraints:
#    1 <= n <= 20
#    1 <= requests.length <= 16
#    requests[i].length == 2
#    0 <= fromi, toi < n

from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """
        Enumerate all subsets of requests using bitmask.
        Check if net change for each building is zero.
        """
        m = len(requests)
        max_requests = 0

        for mask in range(1 << m):
            # Count net change for each building
            balance = [0] * n

            count = 0
            for i in range(m):
                if mask & (1 << i):
                    count += 1
                    from_b, to_b = requests[i]
                    balance[from_b] -= 1
                    balance[to_b] += 1

            # Check if all buildings have zero net change
            if all(b == 0 for b in balance):
                max_requests = max(max_requests, count)

        return max_requests


class SolutionBacktrack:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """
        Backtracking with pruning.
        """
        m = len(requests)
        self.max_count = 0
        balance = [0] * n

        def backtrack(idx: int, count: int):
            if idx == m:
                if all(b == 0 for b in balance):
                    self.max_count = max(self.max_count, count)
                return

            # Pruning: remaining requests can't improve result
            if count + (m - idx) <= self.max_count:
                return

            # Option 1: Include current request
            from_b, to_b = requests[idx]
            balance[from_b] -= 1
            balance[to_b] += 1
            backtrack(idx + 1, count + 1)
            balance[from_b] += 1
            balance[to_b] -= 1

            # Option 2: Exclude current request
            backtrack(idx + 1, count)

        backtrack(0, 0)
        return self.max_count


class SolutionOptimized:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """
        Optimized enumeration: start from largest subsets.
        """
        m = len(requests)

        def is_valid(mask: int) -> bool:
            balance = [0] * n
            for i in range(m):
                if mask & (1 << i):
                    balance[requests[i][0]] -= 1
                    balance[requests[i][1]] += 1
            return all(b == 0 for b in balance)

        # Check from largest to smallest subset size
        for size in range(m, -1, -1):
            # Generate all subsets of given size
            for mask in range(1 << m):
                if bin(mask).count('1') == size and is_valid(mask):
                    return size

        return 0
