#1960. Maximum Product of the Length of Two Palindromic Substrings
#Hard
#
#You are given a 0-indexed string s and are tasked with finding two non-
#intersecting palindromic substrings of odd length such that the product of
#their lengths is maximized.
#
#More formally, you want to choose four integers i, j, k, l such that
#0 <= i <= j < k <= l < n and both the substrings s[i...j] and s[k...l] are
#palindromes and have odd lengths. s[i...j] denotes a substring from index i
#to index j inclusive.
#
#Return the maximum possible product of the lengths of the two non-intersecting
#palindromic substrings.
#
#Example 1:
#Input: s = "ababbb"
#Output: 9
#Explanation: Palindromic substrings "aba" (length 3) and "bbb" (length 3).
#Product = 3 * 3 = 9.
#
#Example 2:
#Input: s = "zaaaxbbby"
#Output: 9
#
#Constraints:
#    2 <= s.length <= 10^5
#    s consists of lowercase English letters.

class Solution:
    def maxProduct(self, s: str) -> int:
        """
        Use Manacher's algorithm to find palindrome radii,
        then compute max odd palindrome ending at/before each position
        and starting at/after each position.
        """
        n = len(s)

        # Manacher's algorithm
        d = [0] * n  # d[i] = radius of longest odd palindrome centered at i

        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # max_left[i] = length of longest odd palindrome ending at or before i
        max_left = [0] * n
        deque = []  # (end position, length)

        j = 0
        for i in range(n):
            # Add palindromes centered at positions up to i
            while j <= i:
                end = j + d[j] - 1
                length = 2 * d[j] - 1
                while deque and deque[-1][0] >= end:
                    deque.pop()
                deque.append((end, length))
                j += 1

            # Remove palindromes that ended before i
            while deque and deque[0][0] < i:
                deque.pop(0)

            # Find max length for position i
            # Use monotonic deque or different approach
            max_left[i] = 1

        # Simplified approach with prefix max
        # max_left[i] = max length of odd palindrome fully in [0, i]
        max_left = [1] * n
        for center in range(n):
            radius = d[center]
            # This palindrome spans [center - radius + 1, center + radius - 1]
            right = center + radius - 1
            length = 2 * radius - 1
            if right < n:
                max_left[right] = max(max_left[right], length)

        # Propagate: shrink palindromes to update positions
        for i in range(n):
            if max_left[i] >= 3:
                if i >= 1:
                    max_left[i - 1] = max(max_left[i - 1], max_left[i] - 2)

        # Take running maximum
        for i in range(1, n):
            max_left[i] = max(max_left[i], max_left[i - 1])

        # max_right[i] = max length of odd palindrome fully in [i, n-1]
        max_right = [1] * n
        for center in range(n):
            radius = d[center]
            left = center - radius + 1
            length = 2 * radius - 1
            if left >= 0:
                max_right[left] = max(max_right[left], length)

        for i in range(n - 1, -1, -1):
            if max_right[i] >= 3:
                if i + 1 < n:
                    max_right[i + 1] = max(max_right[i + 1], max_right[i] - 2)

        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i], max_right[i + 1])

        # Find maximum product
        result = 0
        for i in range(n - 1):
            result = max(result, max_left[i] * max_right[i + 1])

        return result
