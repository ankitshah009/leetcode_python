#922. Sort Array By Parity II
#Easy
#
#Given an array of integers nums, half of the integers in nums are odd, and the
#other half are even.
#
#Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i]
#is even, i is even.
#
#Return any answer array that satisfies this condition.
#
#Example 1:
#Input: nums = [4,2,5,7]
#Output: [4,5,2,7]
#Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also be accepted.
#
#Example 2:
#Input: nums = [2,3]
#Output: [2,3]
#
#Constraints:
#    2 <= nums.length <= 2 * 10^4
#    nums.length is even.
#    Half of the integers in nums are even.
#    0 <= nums[i] <= 1000

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        """
        Two pointers: one for even indices, one for odd.
        """
        n = len(nums)
        even_idx = 0
        odd_idx = 1

        while even_idx < n and odd_idx < n:
            # Find misplaced even number at odd index
            while even_idx < n and nums[even_idx] % 2 == 0:
                even_idx += 2
            # Find misplaced odd number at even index
            while odd_idx < n and nums[odd_idx] % 2 == 1:
                odd_idx += 2

            if even_idx < n and odd_idx < n:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
                even_idx += 2
                odd_idx += 2

        return nums


class SolutionNewArray:
    """Create new array"""

    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        even_idx = 0
        odd_idx = 1

        for num in nums:
            if num % 2 == 0:
                result[even_idx] = num
                even_idx += 2
            else:
                result[odd_idx] = num
                odd_idx += 2

        return result


class SolutionSeparate:
    """Separate then merge"""

    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 == 1]

        result = []
        for e, o in zip(evens, odds):
            result.extend([e, o])

        return result
