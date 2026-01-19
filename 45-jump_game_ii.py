#45. Jump Game II
#Medium
#
#You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
#Each element nums[i] represents the maximum length of a forward jump from index i.
#
#Return the minimum number of jumps to reach nums[n - 1].
#
#The test cases are generated such that you can reach nums[n - 1].
#
#Example 1:
#Input: nums = [2,3,1,1,4]
#Output: 2
#Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#Example 2:
#Input: nums = [2,3,0,1,4]
#Output: 2
#
#Constraints:
#    1 <= nums.length <= 10^4
#    0 <= nums[i] <= 1000
#    It's guaranteed that you can reach nums[n - 1].

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n - 1:
                    break

        return jumps
