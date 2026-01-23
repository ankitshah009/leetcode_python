#857. Minimum Cost to Hire K Workers
#Hard
#
#There are n workers. You are given two integer arrays quality and wage where
#quality[i] is the quality of the ith worker and wage[i] is the minimum wage
#expectation for the ith worker.
#
#We want to hire exactly k workers to form a paid group. To hire a group of k
#workers, we must pay them according to the following rules:
#- Every worker in the paid group should be paid in the ratio of their quality
#  compared to other workers in the paid group.
#- Every worker in the paid group must be paid at least their minimum wage expectation.
#
#Given the integer k, return the least amount of money needed to form a paid
#group satisfying the above conditions. Answers within 10^-5 of the actual answer
#will be accepted.
#
#Example 1:
#Input: quality = [10,20,5], wage = [70,50,30], k = 2
#Output: 105.00000
#
#Example 2:
#Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
#Output: 30.66667
#
#Constraints:
#    n == quality.length == wage.length
#    1 <= k <= n <= 10^4
#    1 <= quality[i], wage[i] <= 10^4

import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        """
        Sort by wage/quality ratio.
        For each worker as the "captain" (determining the ratio),
        pick k-1 workers with lowest quality among those with lower ratio.
        """
        n = len(quality)

        # (ratio, quality) pairs sorted by ratio
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])

        # Max-heap of qualities (negative for max-heap)
        quality_heap = []
        quality_sum = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(quality_heap, -q)
            quality_sum += q

            if len(quality_heap) > k:
                # Remove highest quality worker
                quality_sum += heapq.heappop(quality_heap)  # Adding negative

            if len(quality_heap) == k:
                # Cost = ratio * sum of qualities
                min_cost = min(min_cost, ratio * quality_sum)

        return min_cost


class SolutionExplained:
    """With detailed explanation"""

    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        """
        Key insight:
        - If worker i is paid at ratio r per quality unit, they get r * quality[i]
        - Worker i is satisfied if r * quality[i] >= wage[i], i.e., r >= wage[i]/quality[i]
        - So r must be >= max ratio of all workers in the group
        - Total cost = r * sum(qualities)
        - To minimize: pick smallest sum of qualities with valid ratio
        """
        workers = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])

        heap = []  # Max-heap of qualities
        total_quality = 0
        result = float('inf')

        for q, w in workers:
            ratio = w / q
            heapq.heappush(heap, -q)
            total_quality += q

            if len(heap) > k:
                total_quality += heapq.heappop(heap)

            if len(heap) == k:
                result = min(result, ratio * total_quality)

        return result
