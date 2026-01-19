#2616. Minimize the Maximum Difference of Pairs
#Medium
#
#You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of
#nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no
#index appears more than once amongst the p pairs.
#
#Note that for a pair of elements at the index i and j, the difference of this pair is
#|nums[i] - nums[j]|, where |x| represents the absolute value of x.
#
#Return the minimum maximum difference among all p pairs. We define the maximum of an empty
#set to be zero.
#
#Example 1:
#Input: nums = [10,1,2,7,1,3], p = 2
#Output: 1
#Explanation: The first pair is formed from the indices 1 and 4, and the second pair is
#formed from the indices 2 and 5.
#The maximum difference amongst all the pairs is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|)
#= max(0, 1) = 1. Therefore, we return 1.
#
#Example 2:
#Input: nums = [4,2,1,2], p = 1
#Output: 0
#Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is
#|2 - 2| = 0, which is the minimum we can attain.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^9
#    0 <= p <= (nums.length)/2

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()

        def can_form_pairs(max_diff):
            # Greedy: count pairs with difference <= max_diff
            pairs = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    pairs += 1
                    i += 2  # Skip both elements
                else:
                    i += 1
            return pairs >= p

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = left + (right - left) // 2

            if can_form_pairs(mid):
                right = mid
            else:
                left = mid + 1

        return left
