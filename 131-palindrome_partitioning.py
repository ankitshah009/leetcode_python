#131. Palindrome Partitioning
#Medium
#
#Given a string s, partition s such that every substring of the partition is a palindrome.
#Return all possible palindrome partitioning of s.
#
#Example 1:
#Input: s = "aab"
#Output: [["a","a","b"],["aa","b"]]
#
#Example 2:
#Input: s = "a"
#Output: [["a"]]
#
#Constraints:
#    1 <= s.length <= 16
#    s contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result
