#1664. Ways to Make a Fair Array
#Medium
#
#You are given an integer array nums. You can choose exactly one index and
#remove the element. Array becomes fair when the sum of odd-indexed values
#equals the sum of even-indexed values.
#
#Return the number of indices that you could choose such that after the removal,
#nums is fair.
#
#Example 1:
#Input: nums = [2,1,6,4]
#Output: 1
#Explanation: Remove index 1: [2,6,4]. Odd sum = 6, even sum = 2+4 = 6. Fair.
#
#Example 2:
#Input: nums = [1,1,1]
#Output: 3
#Explanation: Removing any element results in fair array.
#
#Example 3:
#Input: nums = [1,2,3]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^4

from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        """
        Prefix sums for odd and even indices.
        After removing index i:
        - Elements before i keep their parity
        - Elements after i swap parity
        """
        n = len(nums)

        # Compute total odd and even sums
        even_sum = sum(nums[i] for i in range(0, n, 2))
        odd_sum = sum(nums[i] for i in range(1, n, 2))

        count = 0
        left_even = 0
        left_odd = 0

        for i in range(n):
            # After removal:
            # New even = left_even + right_odd
            # New odd = left_odd + right_even

            if i % 2 == 0:
                right_even = even_sum - left_even - nums[i]
                right_odd = odd_sum - left_odd
            else:
                right_even = even_sum - left_even
                right_odd = odd_sum - left_odd - nums[i]

            new_even = left_even + right_odd
            new_odd = left_odd + right_even

            if new_even == new_odd:
                count += 1

            # Update left sums
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]

        return count


class SolutionPrefixArrays:
    def waysToMakeFair(self, nums: List[int]) -> int:
        """
        Using explicit prefix and suffix arrays.
        """
        n = len(nums)

        # Prefix sums
        prefix_even = [0] * (n + 1)
        prefix_odd = [0] * (n + 1)

        for i in range(n):
            prefix_even[i + 1] = prefix_even[i] + (nums[i] if i % 2 == 0 else 0)
            prefix_odd[i + 1] = prefix_odd[i] + (nums[i] if i % 2 == 1 else 0)

        # Suffix sums
        suffix_even = [0] * (n + 1)
        suffix_odd = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix_even[i] = suffix_even[i + 1] + (nums[i] if i % 2 == 0 else 0)
            suffix_odd[i] = suffix_odd[i + 1] + (nums[i] if i % 2 == 1 else 0)

        count = 0

        for i in range(n):
            # After removing i:
            # Even = prefix_even[i] + suffix_odd[i+1]
            # Odd = prefix_odd[i] + suffix_even[i+1]
            new_even = prefix_even[i] + suffix_odd[i + 1]
            new_odd = prefix_odd[i] + suffix_even[i + 1]

            if new_even == new_odd:
                count += 1

        return count


class SolutionCompact:
    def waysToMakeFair(self, nums: List[int]) -> int:
        """
        Compact implementation with running sums.
        """
        n = len(nums)
        total = [0, 0]  # [even_sum, odd_sum]

        for i, num in enumerate(nums):
            total[i % 2] += num

        left = [0, 0]
        count = 0

        for i, num in enumerate(nums):
            total[i % 2] -= num

            # new_even = left[0] + total[1]
            # new_odd = left[1] + total[0]
            if left[0] + total[1] == left[1] + total[0]:
                count += 1

            left[i % 2] += num

        return count


class SolutionDetailed:
    def waysToMakeFair(self, nums: List[int]) -> int:
        """
        More detailed implementation with comments.
        """
        n = len(nums)
        count = 0

        # Track sums of even and odd indexed elements
        even_right = sum(nums[i] for i in range(0, n, 2))
        odd_right = sum(nums[i] for i in range(1, n, 2))
        even_left = 0
        odd_left = 0

        for i in range(n):
            # Remove current element from right sum
            if i % 2 == 0:
                even_right -= nums[i]
            else:
                odd_right -= nums[i]

            # Check if fair after removal
            # After removal, right elements swap parity
            total_even = even_left + odd_right
            total_odd = odd_left + even_right

            if total_even == total_odd:
                count += 1

            # Add current element to left sum
            if i % 2 == 0:
                even_left += nums[i]
            else:
                odd_left += nums[i]

        return count
