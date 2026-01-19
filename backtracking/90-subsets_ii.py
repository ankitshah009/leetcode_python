#90. Subsets II
#Medium
#
#Given an integer array nums that may contain duplicates, return all possible subsets
#(the power set).
#
#The solution set must not contain duplicate subsets. Return the solution in any order.
#
#Example 1:
#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#Example 2:
#Input: nums = [0]
#Output: [[],[0]]
#
#Constraints:
#    1 <= nums.length <= 10
#    -10 <= nums[i] <= 10

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result
