#1723. Find Minimum Time to Finish All Jobs
#Hard
#
#You are given an integer array jobs, where jobs[i] is the amount of time it
#takes to complete the ith job.
#
#There are k workers that you can assign jobs to. Each job should be assigned to
#exactly one worker. The working time of a worker is the sum of the time it
#takes to complete all jobs assigned to them. Your goal is to devise an optimal
#assignment such that the maximum working time of any worker is minimized.
#
#Return the minimum possible maximum working time of any assignment.
#
#Example 1:
#Input: jobs = [3,2,3], k = 3
#Output: 3
#
#Example 2:
#Input: jobs = [1,2,4,7,8], k = 2
#Output: 11
#
#Constraints:
#    1 <= k <= jobs.length <= 12
#    1 <= jobs[i] <= 10^7

from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        Binary search + backtracking.
        Binary search on answer, check if valid with backtracking.
        """
        jobs.sort(reverse=True)  # Assign larger jobs first for better pruning

        def can_finish(limit: int) -> bool:
            workers = [0] * k

            def backtrack(job_idx: int) -> bool:
                if job_idx == len(jobs):
                    return True

                seen = set()  # Avoid assigning same workload to different workers
                for i in range(k):
                    if workers[i] in seen:
                        continue
                    if workers[i] + jobs[job_idx] <= limit:
                        seen.add(workers[i])
                        workers[i] += jobs[job_idx]
                        if backtrack(job_idx + 1):
                            return True
                        workers[i] -= jobs[job_idx]

                return False

            return backtrack(0)

        left = max(jobs)
        right = sum(jobs)

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left


class SolutionDP:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        Bitmask DP approach.
        """
        n = len(jobs)

        # Precompute sum for each subset of jobs
        subset_sum = [0] * (1 << n)
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    subset_sum[mask] += jobs[i]

        # dp[i][mask] = min max time using i workers for subset mask
        # Optimize: dp[mask] for current number of workers
        dp = subset_sum[:]  # 1 worker handles all

        for _ in range(1, k):
            new_dp = [float('inf')] * (1 << n)
            for mask in range(1 << n):
                # Try all subsets of mask for current worker
                subset = mask
                while subset:
                    remaining = mask ^ subset
                    new_dp[mask] = min(new_dp[mask],
                                       max(subset_sum[subset], dp[remaining]))
                    subset = (subset - 1) & mask
            dp = new_dp

        return dp[(1 << n) - 1]


class SolutionBacktrack:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        Pure backtracking with pruning.
        """
        jobs.sort(reverse=True)
        n = len(jobs)
        workers = [0] * k
        self.result = sum(jobs)

        def backtrack(idx: int, current_max: int):
            if current_max >= self.result:
                return

            if idx == n:
                self.result = current_max
                return

            seen = set()
            for i in range(k):
                if workers[i] in seen:
                    continue
                seen.add(workers[i])

                workers[i] += jobs[idx]
                backtrack(idx + 1, max(current_max, workers[i]))
                workers[i] -= jobs[idx]

        backtrack(0, 0)
        return self.result
