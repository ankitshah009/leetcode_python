#2462. Total Cost to Hire K Workers
#Medium
#
#You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the
#ith worker.
#
#You are also given two integers k and candidates. We want to hire exactly k workers
#according to the following rules:
#    You will run k sessions and hire exactly one worker in each session.
#    In each hiring session, choose the worker with the lowest cost from either the first
#        candidates workers or the last candidates workers. Break the tie by the smallest index.
#    If there are fewer than candidates workers remaining, choose the worker with the
#        lowest cost among them. Break the tie by the smallest index.
#    A worker can only be chosen once.
#
#Return the total cost to hire exactly k workers.
#
#Example 1:
#Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
#Output: 11
#Explanation: We hire 3 workers in total. The total cost is initially 0.
#- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8].
#  The lowest cost is 2, and we break the tie by the smallest index, which is 3.
#  The total cost = 0 + 2 = 2.
#- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8].
#  The lowest cost is 2, and we break the tie by the smallest index, which is 4.
#  The total cost = 2 + 2 = 4.
#- In the third hiring round we choose the worker from [17,12,10,7,11,20,8].
#  The lowest cost is 7, and we break the tie by the smallest index, which is 3.
#  The total cost = 4 + 7 = 11.
#The total hiring cost is 11.
#
#Example 2:
#Input: costs = [1,2,4,1], k = 3, candidates = 3
#Output: 4
#
#Constraints:
#    1 <= costs.length <= 10^5
#    1 <= costs[i] <= 10^5
#    1 <= k, candidates <= costs.length

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total = 0

        # Two heaps for front and back candidates
        front_heap = []
        back_heap = []

        left = 0
        right = n - 1

        # Initialize front candidates
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(front_heap, (costs[left], left))
                left += 1

        # Initialize back candidates
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(back_heap, (costs[right], right))
                right -= 1

        for _ in range(k):
            # Get minimum from both heaps
            if not back_heap or (front_heap and front_heap[0] <= back_heap[0]):
                cost, idx = heapq.heappop(front_heap)
                total += cost
                # Add next from front if available
                if left <= right:
                    heapq.heappush(front_heap, (costs[left], left))
                    left += 1
            else:
                cost, idx = heapq.heappop(back_heap)
                total += cost
                # Add next from back if available
                if left <= right:
                    heapq.heappush(back_heap, (costs[right], right))
                    right -= 1

        return total
