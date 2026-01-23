#1674. Minimum Moves to Make Array Complementary
#Medium
#
#You are given an integer array nums of even length n and an integer limit.
#In one move, you can replace any integer from nums with another integer
#between 1 and limit, inclusive.
#
#The array nums is complementary if for all indices i (0-indexed), nums[i] +
#nums[n - 1 - i] equals the same number. For example, [1,2,3,4] is complementary
#because for all i, nums[i] + nums[n-1-i] = 5.
#
#Return the minimum number of moves required to make nums complementary.
#
#Example 1:
#Input: nums = [1,2,4,3], limit = 4
#Output: 1
#Explanation: In 1 move, change nums[2] to 2. nums becomes [1,2,2,3].
#All pairs sum to 4.
#
#Example 2:
#Input: nums = [1,2,2,1], limit = 2
#Output: 2
#
#Example 3:
#Input: nums = [1,2,1,2], limit = 2
#Output: 0
#
#Constraints:
#    n == nums.length
#    2 <= n <= 10^5
#    1 <= nums[i] <= limit <= 10^5
#    n is even.

from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        Difference array approach.
        For each pair, analyze ranges of possible target sums.
        """
        n = len(nums)
        # diff[s] = change in cost when target sum goes from s-1 to s
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]

            # For target sum T:
            # - If T < min(a,b) + 1 or T > max(a,b) + limit: need 2 moves
            # - If min(a,b) + 1 <= T < a+b or a+b < T <= max(a,b) + limit: need 1 move
            # - If T == a + b: need 0 moves

            lo = min(a, b) + 1
            hi = max(a, b) + limit
            curr_sum = a + b

            # Default: 2 moves for all sums
            # Range [lo, hi]: need at most 1 move
            # At curr_sum: need 0 moves

            diff[2] += 2       # Start with 2 moves for range [2, 2*limit]
            diff[lo] -= 1      # Range [lo, hi] needs only 1 move
            diff[curr_sum] -= 1  # At curr_sum, needs 0 moves
            diff[curr_sum + 1] += 1  # After curr_sum, back to 1 move
            diff[hi + 1] += 1  # After hi, back to 2 moves

        # Compute prefix sum and find minimum
        min_moves = float('inf')
        curr = 0

        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            min_moves = min(min_moves, curr)

        return min_moves


class SolutionBruteForce:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        Brute force: try all possible target sums.
        O(n * limit) - may TLE for large inputs.
        """
        n = len(nums)
        min_moves = float('inf')

        for target in range(2, 2 * limit + 1):
            moves = 0
            for i in range(n // 2):
                a, b = nums[i], nums[n - 1 - i]
                curr_sum = a + b

                if curr_sum == target:
                    continue  # 0 moves
                elif (min(a, b) + 1 <= target <= max(a, b) + limit):
                    moves += 1  # 1 move
                else:
                    moves += 2  # 2 moves

            min_moves = min(min_moves, moves)

        return min_moves


class SolutionDetailed:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        Detailed difference array implementation.
        """
        n = len(nums)

        # delta[t] = cost[t] - cost[t-1]
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo, hi = min(a, b), max(a, b)
            pair_sum = a + b

            # Range [2, lo]: 2 moves (must change both)
            # Range [lo+1, pair_sum-1]: 1 move (can change one to reach)
            # Target = pair_sum: 0 moves
            # Range [pair_sum+1, hi+limit]: 1 move
            # Range [hi+limit+1, 2*limit]: 2 moves

            # Use delta to track changes
            # At 2: +2 (all start at 2 cost)
            delta[2] += 2
            # At lo+1: -1 (cost goes from 2 to 1)
            delta[lo + 1] -= 1
            # At pair_sum: -1 (cost goes from 1 to 0)
            delta[pair_sum] -= 1
            # At pair_sum+1: +1 (cost goes from 0 to 1)
            delta[pair_sum + 1] += 1
            # At hi+limit+1: +1 (cost goes from 1 to 2)
            delta[hi + limit + 1] += 1

        # Compute cumulative sum
        ans = float('inf')
        cost = 0

        for t in range(2, 2 * limit + 1):
            cost += delta[t]
            ans = min(ans, cost)

        return ans
