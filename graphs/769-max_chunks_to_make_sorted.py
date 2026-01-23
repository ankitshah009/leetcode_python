#769. Max Chunks To Make Sorted
#Medium
#
#You are given an integer array arr of length n that represents a permutation
#of the integers in the range [0, n - 1].
#
#We split arr into some number of chunks (i.e., partitions), and individually
#sort each chunk. After concatenating them, the result should equal the sorted
#array.
#
#Return the largest number of chunks we can make to sort the array.
#
#Example 1:
#Input: arr = [4,3,2,1,0]
#Output: 1
#Explanation: Splitting into two or more chunks will not return the required
#result. For example, splitting into [4, 3], [2, 1, 0] will result in
#[3, 4, 0, 1, 2], which isn't sorted.
#
#Example 2:
#Input: arr = [1,0,2,3,4]
#Output: 4
#Explanation: We can split into two chunks, such as [1, 0], [2, 3, 4].
#However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks.
#
#Constraints:
#    n == arr.length
#    1 <= n <= 10
#    0 <= arr[i] < n
#    All the elements of arr are unique.

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        """
        Key insight: can cut after index i if max(arr[0..i]) == i.
        Because sorted array has value i at index i.
        """
        chunks = 0
        max_val = 0

        for i, num in enumerate(arr):
            max_val = max(max_val, num)
            if max_val == i:
                chunks += 1

        return chunks


class SolutionStack:
    """Stack-based approach (same as problem 768)"""

    def maxChunksToSorted(self, arr: list[int]) -> int:
        stack = []

        for num in arr:
            if not stack or num >= stack[-1]:
                stack.append(num)
            else:
                max_val = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(max_val)

        return len(stack)


class SolutionSum:
    """Compare running sums"""

    def maxChunksToSorted(self, arr: list[int]) -> int:
        # Sum of arr[0..i] should equal sum of [0..i] to be valid cut
        chunks = 0
        sum_arr = 0
        expected_sum = 0

        for i, num in enumerate(arr):
            sum_arr += num
            expected_sum += i

            if sum_arr == expected_sum:
                chunks += 1

        return chunks


class SolutionMinMax:
    """Using prefix max and suffix min"""

    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        chunks = 0

        prefix_max = -1

        for i in range(n):
            prefix_max = max(prefix_max, arr[i])
            if prefix_max == i:
                chunks += 1

        return chunks
