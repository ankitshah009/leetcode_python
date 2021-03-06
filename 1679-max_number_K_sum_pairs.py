#1679. Max Number of K-Sum Pairs
#Medium
#
#You are given an integer array nums and an integer k.
#
#In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
#Return the maximum number of operations you can perform on the array.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,4], k = 5
#Output: 2
#Explanation: Starting with nums = [1,2,3,4]:
#- Remove numbers 1 and 4, then nums = [2,3]
#- Remove numbers 2 and 3, then nums = []
#There are no more pairs that sum up to 5, hence a total of 2 operations.
#
#Example 2:
#
#Input: nums = [3,1,3,4,3], k = 6
#Output: 1
#Explanation: Starting with nums = [3,1,3,4,3]:
#- Remove the first two 3's, then nums = [1,4,3]
#There are no more pairs that sum up to 6, hence a total of 1 operation.
#
# 
#
#Constraints:
#
#    1 <= nums.length <= 105
#    1 <= nums[i] <= 109
#    1 <= k <= 109
#


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d=collections.Counter(nums)
        c=0    
        for i in nums:
            if(d[i]>0):
                d[i]-=1
                if(d[k-i]>0):
                    d[k-i]-=1
                    c+=1
        
        return c

#### This is O(N) but over the unique keys - Not my solution - but smarter way of iterating. 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_nums = collections.Counter(nums)
        result = 0
        for num in count_nums:
            target = max(0, k - num)
            if target == num:
                result += count_nums[num] // 2
            else:
                result += min(count_nums[num], count_nums[target])
            count_nums[num] = 0
        return result
