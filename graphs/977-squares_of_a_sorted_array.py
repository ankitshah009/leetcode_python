#977. Squares of a Sorted Array
#Easy
#
#Given an integer array nums sorted in non-decreasing order, return an array of
#the squares of each number sorted in non-decreasing order.
#
#Example 1:
#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
#
#Example 2:
#Input: nums = [-7,-3,2,3,11]
#Output: [4,9,9,49,121]
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -10^4 <= nums[i] <= 10^4
#    nums is sorted in non-decreasing order.
#
#Follow up: Squaring each element and sorting the new array is very trivial,
#could you find an O(n) solution using a different approach?

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        Two pointers from both ends (largest squares at ends).
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq >= right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1

            pos -= 1

        return result


class SolutionSimple:
    """Simple square and sort"""

    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(x * x for x in nums)


class SolutionMerge:
    """Find split point and merge"""

    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Find first non-negative
        split = 0
        while split < n and nums[split] < 0:
            split += 1

        # Merge two parts
        result = []
        left = split - 1  # Negatives going left
        right = split  # Non-negatives going right

        while left >= 0 and right < n:
            if -nums[left] <= nums[right]:
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1

        while left >= 0:
            result.append(nums[left] ** 2)
            left -= 1

        while right < n:
            result.append(nums[right] ** 2)
            right += 1

        return result
