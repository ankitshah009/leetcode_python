#47. Permutations II
#Medium
#
#Given a collection of numbers, nums, that might contain duplicates, return all possible
#unique permutations in any order.
#
#Example 1:
#Input: nums = [1,1,2]
#Output: [[1,1,2],[1,2,1],[2,1,1]]
#
#Example 2:
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#Constraints:
#    1 <= nums.length <= 8
#    -10 <= nums[i] <= 10

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(current, remaining):
            if not remaining:
                result.append(current[:])
                return

            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i + 1:])
                current.pop()

        backtrack([], nums)
        return result
