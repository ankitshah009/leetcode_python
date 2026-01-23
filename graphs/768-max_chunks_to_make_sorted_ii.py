#768. Max Chunks To Make Sorted II
#Hard
#
#You are given an integer array arr.
#
#We split arr into some number of chunks (i.e., partitions), and individually
#sort each chunk. After concatenating them, the result should equal the sorted
#array.
#
#Return the largest number of chunks we can make to sort the array.
#
#Example 1:
#Input: arr = [5,4,3,2,1]
#Output: 1
#Explanation: Splitting into two or more chunks will not return the required
#result. For example, splitting into [5, 4], [3, 2, 1] will result in
#[4, 5, 1, 2, 3], which isn't sorted.
#
#Example 2:
#Input: arr = [2,1,3,4,4]
#Output: 4
#Explanation: We can split into two chunks, such as [2, 1], [3, 4, 4].
#However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks.
#
#Constraints:
#    1 <= arr.length <= 2000
#    0 <= arr[i] <= 10^8

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        """
        Use monotonic stack: can cut when max of left chunk <= min of right.
        """
        stack = []  # Stack of max values of each chunk

        for num in arr:
            if not stack or num >= stack[-1]:
                stack.append(num)
            else:
                # Merge chunks: keep the max of merged chunk
                max_val = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(max_val)

        return len(stack)


class SolutionPrefixMax:
    """Compare prefix max with sorted array"""

    def maxChunksToSorted(self, arr: list[int]) -> int:
        sorted_arr = sorted(arr)
        chunks = 0
        sum_arr = sum_sorted = 0

        for i in range(len(arr)):
            sum_arr += arr[i]
            sum_sorted += sorted_arr[i]

            if sum_arr == sum_sorted:
                chunks += 1

        return chunks


class SolutionCounting:
    """Using counting approach"""

    def maxChunksToSorted(self, arr: list[int]) -> int:
        from collections import Counter

        sorted_arr = sorted(arr)
        chunks = 0
        count = Counter()

        for i in range(len(arr)):
            count[arr[i]] += 1
            count[sorted_arr[i]] -= 1

            if count[arr[i]] == 0:
                del count[arr[i]]
            if count[sorted_arr[i]] == 0:
                del count[sorted_arr[i]]

            if not count:
                chunks += 1

        return chunks


class SolutionMinMax:
    """Using prefix max and suffix min"""

    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)

        # prefix_max[i] = max of arr[0..i]
        prefix_max = [0] * n
        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        # suffix_min[i] = min of arr[i..n-1]
        suffix_min = [0] * n
        suffix_min[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])

        # Count chunks: can cut after i if prefix_max[i] <= suffix_min[i+1]
        chunks = 1  # Last chunk always counted
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:
                chunks += 1

        return chunks
