#1415. The k-th Lexicographical String of All Happy Strings of Length n
#Medium
#
#A happy string is a string that:
#    consists only of letters of the set ['a', 'b', 'c'].
#    s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
#    1-indexed).
#
#For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings
#and strings "aa", "baa" and "ababbc" are not happy strings.
#
#Given two integers n and k, consider a list of all happy strings of length n
#sorted in lexicographical order.
#
#Return the kth string of this list or return an empty string if there are less
#than k happy strings of length n.
#
#Example 1:
#Input: n = 1, k = 3
#Output: "c"
#Explanation: The list ["a", "b", "c"] contains all happy strings of length 1.
#The third string is "c".
#
#Example 2:
#Input: n = 1, k = 4
#Output: ""
#Explanation: There are only 3 happy strings of length 1.
#
#Example 3:
#Input: n = 3, k = 9
#Output: "cab"
#Explanation: There are 12 different happy string of length 3
#["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"].
#You will find the 9th string = "cab"
#
#Constraints:
#    1 <= n <= 10
#    1 <= k <= 100

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Generate all happy strings in lexicographical order.
        Total count: 3 * 2^(n-1) (first char has 3 choices, rest have 2).
        """
        happy_strings = []

        def backtrack(current: str):
            if len(current) == n:
                happy_strings.append(current)
                return

            for c in 'abc':
                if not current or current[-1] != c:
                    backtrack(current + c)
                    if len(happy_strings) >= k:
                        return

        backtrack('')

        return happy_strings[k - 1] if k <= len(happy_strings) else ''


class SolutionDirect:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Directly compute kth string without generating all.
        There are 3 * 2^(n-1) happy strings total.
        First char divides into 3 groups of 2^(n-1) each.
        """
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ''

        result = []
        k -= 1  # 0-indexed

        # First character
        group_size = 2 ** (n - 1)
        first_char_idx = k // group_size
        result.append('abc'[first_char_idx])
        k %= group_size

        # Remaining characters
        for _ in range(n - 1):
            group_size //= 2
            # Two choices: characters that aren't the previous one
            prev = result[-1]
            choices = [c for c in 'abc' if c != prev]

            char_idx = k // group_size
            result.append(choices[char_idx])
            k %= group_size

        return ''.join(result)


class SolutionIterative:
    def getHappyString(self, n: int, k: int) -> str:
        """Iterative generation"""
        from collections import deque

        queue = deque(['a', 'b', 'c'])
        count = 0

        while queue:
            current = queue.popleft()

            if len(current) == n:
                count += 1
                if count == k:
                    return current
                continue

            for c in 'abc':
                if current[-1] != c:
                    queue.append(current + c)

        return ''
