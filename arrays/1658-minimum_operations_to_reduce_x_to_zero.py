#1658. Minimum Operations to Reduce X to Zero
#Medium
#
#You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
#
#Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.
#
# 
#
#Example 1:
#
#Input: nums = [1,1,4,2,3], x = 5
#Output: 2
#Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
#
#Example 2:
#
#Input: nums = [5,6,7,8,9], x = 4
#Output: -1
#
#Example 3:
#
#Input: nums = [3,2,20,1,1,3], x = 10
#Output: 5
#Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
#
# 
#
#Constraints:
#
#    1 <= nums.length <= 105
#    1 <= nums[i] <= 104
#    1 <= x <= 109
#

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        val = sum(nums)
        if x > val: return -1   # Even use all nums can't subtract x to zero
        elif x == val: return len(nums)   # Need all nums to complete mission (shortcut)
        
        # left for left bound, right for right bound
        nums.append(0)   # For the case no use right part
        ret, left, right, length = 100000, 0, 0, len(nums)
        while right < length:
            if val > x:   # Too much, move right
                val -= nums[right]
                right += 1
            elif val < x:   # Too less, move left
                val += nums[left]
                left += 1
            else:   # PERFECT, move both
                ret = min(ret, length+left-right-1)
                val = val + nums[left] - nums[right]
                left += 1
                right += 1
        return ret if ret != 100000 else -1

