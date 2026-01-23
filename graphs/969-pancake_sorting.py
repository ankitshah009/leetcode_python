#969. Pancake Sorting
#Medium
#
#Given an array of integers arr, sort the array by performing a series of
#pancake flips.
#
#In one pancake flip we do the following steps:
#- Choose an integer k where 1 <= k <= arr.length.
#- Reverse the sub-array arr[0...k-1] (0-indexed).
#
#Return an array of the k-values corresponding to a sequence of pancake flips
#that sort arr. Any valid answer that sorts the array within 10 * arr.length
#flips will be judged as correct.
#
#Example 1:
#Input: arr = [3,2,4,1]
#Output: [4,2,4,3]
#Explanation: We perform 4 pancake flips, with k = 4, 2, 4, 3.
#
#Example 2:
#Input: arr = [1,2,3]
#Output: []
#
#Constraints:
#    1 <= arr.length <= 100
#    1 <= arr[i] <= arr.length
#    All integers in arr are unique.

class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        """
        Move largest to end, then second largest, etc.
        """
        result = []
        n = len(arr)

        for size in range(n, 1, -1):
            # Find position of max element in arr[0:size]
            max_idx = arr.index(size)

            if max_idx == size - 1:
                continue  # Already in place

            # Flip to bring max to front (if not already there)
            if max_idx > 0:
                arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
                result.append(max_idx + 1)

            # Flip to move max to correct position
            arr[:size] = arr[:size][::-1]
            result.append(size)

        return result


class SolutionExplicit:
    """More explicit flipping"""

    def pancakeSort(self, arr: list[int]) -> list[int]:
        def flip(arr, k):
            """Reverse first k elements."""
            left, right = 0, k - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        result = []
        n = len(arr)

        for i in range(n - 1, 0, -1):
            # Find index of (i+1) in arr[0:i+1]
            max_val = i + 1
            max_idx = arr.index(max_val)

            if max_idx == i:
                continue

            # Flip to bring to front
            if max_idx > 0:
                flip(arr, max_idx + 1)
                result.append(max_idx + 1)

            # Flip to send to position i
            flip(arr, i + 1)
            result.append(i + 1)

        return result


class SolutionRecursive:
    """Recursive approach"""

    def pancakeSort(self, arr: list[int]) -> list[int]:
        result = []

        def sort(n):
            if n == 1:
                return

            # Find max in arr[0:n]
            max_idx = max(range(n), key=lambda i: arr[i])

            if max_idx != n - 1:
                if max_idx > 0:
                    arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
                    result.append(max_idx + 1)

                arr[:n] = arr[:n][::-1]
                result.append(n)

            sort(n - 1)

        sort(len(arr))
        return result
