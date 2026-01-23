#556. Next Greater Element III
#Medium
#
#Given a positive integer n, find the smallest integer which has exactly the same
#digits existing in the integer n and is greater in value than n. If no such
#positive integer exists, return -1.
#
#Note that the returned integer should fit in 32-bit integer, if there is a valid
#answer but it does not fit in 32-bit integer, return -1.
#
#Example 1:
#Input: n = 12
#Output: 21
#
#Example 2:
#Input: n = 21
#Output: -1
#
#Constraints:
#    1 <= n <= 2^31 - 1

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        Same as "Next Permutation" algorithm:
        1. Find rightmost digit smaller than its right neighbor
        2. Swap with smallest digit larger than it on the right
        3. Reverse the suffix
        """
        digits = list(str(n))
        length = len(digits)

        # Step 1: Find pivot (rightmost digit < right neighbor)
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i < 0:
            return -1  # Already largest permutation

        # Step 2: Find smallest digit larger than pivot on the right
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Swap
        digits[i], digits[j] = digits[j], digits[i]

        # Step 3: Reverse suffix (already in descending order)
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int(''.join(digits))

        # Check 32-bit overflow
        if result > 2**31 - 1:
            return -1

        return result


class SolutionExplicit:
    """More explicit step by step"""

    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))

        # Find first decreasing element from right
        pivot = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        if pivot == -1:
            return -1

        # Find smallest element larger than pivot
        for i in range(len(arr) - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Reverse suffix
        left, right = pivot + 1, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        result = int(''.join(arr))
        return result if result <= 2**31 - 1 else -1
