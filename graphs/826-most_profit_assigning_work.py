#826. Most Profit Assigning Work
#Medium
#
#You have n jobs and m workers. You are given three arrays: difficulty, profit,
#and worker where:
#- difficulty[i] and profit[i] are the difficulty and the profit of the ith job
#- worker[j] is the ability of jth worker (i.e., the jth worker can only
#  complete a job with difficulty at most worker[j]).
#
#Every worker can be assigned at most one job, but one job can be completed
#multiple times.
#
#For example, if three workers attempt the same job that pays $1, then the
#total profit will be $3. If a worker cannot complete any job, their profit is $0.
#
#Return the maximum profit we can achieve after assigning the workers to the jobs.
#
#Example 1:
#Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,1]
#Output: 100
#Explanation: Workers are assigned jobs of difficulty [4,4,6,none] and profits [20,20,30,0].
#
#Example 2:
#Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
#Output: 0
#
#Constraints:
#    n == difficulty.length == profit.length
#    m == worker.length
#    1 <= n, m <= 10^4
#    1 <= difficulty[i], profit[i], worker[i] <= 10^5

class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        """
        Sort jobs by difficulty, maintain max profit seen so far.
        Sort workers and process in order.
        """
        jobs = sorted(zip(difficulty, profit))
        workers = sorted(worker)

        total = 0
        max_profit = 0
        j = 0  # Job index

        for ability in workers:
            # Update max profit for all jobs this worker can do
            while j < len(jobs) and jobs[j][0] <= ability:
                max_profit = max(max_profit, jobs[j][1])
                j += 1

            total += max_profit

        return total


class SolutionBinarySearch:
    """Using binary search"""

    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        from bisect import bisect_right

        # Create (difficulty, profit) pairs and sort
        jobs = sorted(zip(difficulty, profit))

        # Precompute max profit up to each difficulty
        max_profit = [0] * len(jobs)
        max_profit[0] = jobs[0][1]
        for i in range(1, len(jobs)):
            max_profit[i] = max(max_profit[i - 1], jobs[i][1])

        difficulties = [j[0] for j in jobs]

        total = 0
        for ability in worker:
            idx = bisect_right(difficulties, ability) - 1
            if idx >= 0:
                total += max_profit[idx]

        return total


class SolutionBucket:
    """Bucket sort approach"""

    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        max_ability = max(max(worker), max(difficulty))

        # Best profit for each difficulty level
        best = [0] * (max_ability + 1)

        for d, p in zip(difficulty, profit):
            best[d] = max(best[d], p)

        # Convert to max profit for difficulty <= i
        for i in range(1, max_ability + 1):
            best[i] = max(best[i], best[i - 1])

        return sum(best[w] for w in worker)
