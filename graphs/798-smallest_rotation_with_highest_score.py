#798. Smallest Rotation with Highest Score
#Hard
#
#You are given an array nums. You can rotate it by a non-negative integer k so
#that the array becomes [nums[k], nums[k + 1], ... nums[nums.length - 1],
#nums[0], nums[1], ..., nums[k-1]]. Afterward, any entries that are less than
#or equal to their index are worth one point.
#
#For example, if we have nums = [2,4,1,3,0], and we rotate by k = 2, it becomes
#[1,3,0,2,4]. This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points],
#0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
#
#Return the smallest rotation index k that corresponds to the highest score we
#can achieve.
#
#Example 1:
#Input: nums = [2,3,1,4,0]
#Output: 3
#Explanation: Scores for each k:
#k=0: [2,3,1,4,0], score 2
#k=1: [3,1,4,0,2], score 3
#k=2: [1,4,0,2,3], score 3
#k=3: [4,0,2,3,1], score 4
#k=4: [0,2,3,1,4], score 3
#So k=3 is best.
#
#Example 2:
#Input: nums = [1,3,0,2,4]
#Output: 0
#Explanation: nums will always have 3 points no matter how rotated.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] < nums.length

class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        """
        For each element, find range of k where it scores a point.
        Use difference array to count points for each k.

        Element at index i with value v scores when:
        - After rotation by k, new index is (i - k + n) % n
        - It scores if v <= (i - k + n) % n

        For each i, find range of k values that give points.
        """
        n = len(nums)
        # Difference array: change[k] = score change at rotation k
        change = [0] * n

        for i, v in enumerate(nums):
            # Element scores when its new index >= v
            # New index = (i - k + n) % n
            # Scores when (i - k + n) % n >= v

            # Without wrap: k <= i - v, so k in [0, i - v]
            # With wrap: k > i means new_idx = i - k + n
            # Scores when i - k + n >= v, i.e., k <= i + n - v

            # Low k (no wrap): k in [0, i] gives new_idx in [i, 0]
            # Scores when new_idx >= v, i.e., when k <= i - v

            low = (i + 1) % n  # k where we start wrapping
            high = (i - v + n) % n  # highest k that scores (with wrap)

            # Add 1 at start of scoring range, subtract 1 after end
            change[low] += 1
            change[(high + 1) % n] -= 1

            # Handle case where v > i (never scores without wrap)
            if low <= high:
                # Continuous range [low, high]
                pass
            else:
                # Wrap around: [low, n-1] and [0, high]
                # Already handled by difference array
                pass

        # Compute prefix sum to get actual scores
        best_k = 0
        best_score = 0
        score = 0

        for k in range(n):
            score += change[k]
            if score > best_score:
                best_score = score
                best_k = k

        return best_k


class SolutionInterval:
    """Explicit interval tracking"""

    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        bad = [0] * n  # bad[k] = how many elements lose their point at rotation k

        for i, v in enumerate(nums):
            # Element at i loses point when rotated to index < v
            # This happens when k = (i - v + 1 + n) % n
            left = (i - v + 1 + n) % n
            right = (i + 1) % n

            bad[left] -= 1
            bad[right] += 1

            if left > right:
                bad[0] -= 1

        best_k = 0
        best_score = float('-inf')
        score = 0

        for k in range(n):
            score += bad[k]
            if score > best_score:
                best_score = score
                best_k = k

        return best_k
