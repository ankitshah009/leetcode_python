#1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number
#Medium
#
#You are given a string num, representing a large integer, and an integer k.
#
#We call some integer wonderful if it is a permutation of the digits in num and
#is greater in value than num. There can be many wonderful integers. However,
#we only care about the smallest-valued ones.
#
#Return the minimum number of adjacent digit swaps that needs to be applied to
#num to reach the kth smallest wonderful integer.
#
#Example 1:
#Input: num = "5489355142", k = 4
#Output: 2
#
#Example 2:
#Input: num = "11112", k = 4
#Output: 4
#
#Example 3:
#Input: num = "00123", k = 1
#Output: 1
#
#Constraints:
#    2 <= num.length <= 1000
#    1 <= k <= 1000
#    num only consists of digits.

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        """
        1. Find kth next permutation
        2. Count swaps to transform original to kth permutation
        """
        target = list(num)

        # Get kth next permutation
        for _ in range(k):
            self.next_permutation(target)

        # Count swaps needed
        original = list(num)
        return self.count_swaps(original, target)

    def next_permutation(self, arr: list) -> None:
        """Modify arr to next lexicographically greater permutation."""
        n = len(arr)

        # Find rightmost i where arr[i] < arr[i+1]
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            # Find rightmost j where arr[j] > arr[i]
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]

        # Reverse suffix
        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def count_swaps(self, source: list, target: list) -> int:
        """Count adjacent swaps to transform source to target."""
        source = source[:]
        swaps = 0

        for i in range(len(target)):
            if source[i] == target[i]:
                continue

            # Find target[i] in source
            j = i + 1
            while source[j] != target[i]:
                j += 1

            # Bubble it to position i
            while j > i:
                source[j], source[j - 1] = source[j - 1], source[j]
                j -= 1
                swaps += 1

        return swaps


class SolutionDetailed:
    def getMinSwaps(self, num: str, k: int) -> int:
        """
        Same approach with clearer separation.
        """
        def next_perm(s: list) -> None:
            n = len(s)
            i = n - 2
            while i >= 0 and s[i] >= s[i + 1]:
                i -= 1
            if i >= 0:
                j = n - 1
                while s[j] <= s[i]:
                    j -= 1
                s[i], s[j] = s[j], s[i]
            s[i + 1:] = reversed(s[i + 1:])

        def min_swaps(start: list, end: list) -> int:
            start = start[:]
            count = 0
            for i in range(len(start)):
                if start[i] != end[i]:
                    j = i + 1
                    while start[j] != end[i]:
                        j += 1
                    while j > i:
                        start[j], start[j - 1] = start[j - 1], start[j]
                        j -= 1
                        count += 1
            return count

        target = list(num)
        for _ in range(k):
            next_perm(target)

        return min_swaps(list(num), target)
