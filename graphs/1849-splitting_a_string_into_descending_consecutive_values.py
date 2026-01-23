#1849. Splitting a String Into Descending Consecutive Values
#Medium
#
#You are given a string s that consists of only digits.
#
#Check if we can split s into two or more non-empty substrings such that the
#numerical values of the substrings are in descending order and the difference
#between numerical values of every two adjacent substrings is equal to 1.
#
#Note: Adjacent substrings have consecutive indices.
#
#Return true if it is possible to split s as described above, or false
#otherwise.
#
#A substring is a contiguous sequence of characters in a string.
#
#Example 1:
#Input: s = "1234"
#Output: false
#
#Example 2:
#Input: s = "050043"
#Output: true
#
#Example 3:
#Input: s = "9080701"
#Output: false
#
#Constraints:
#    1 <= s.length <= 20
#    s only consists of digits.

class Solution:
    def splitString(self, s: str) -> bool:
        """
        Backtracking: try each first number length.
        """
        def backtrack(index: int, prev: int, count: int) -> bool:
            if index == len(s):
                return count >= 2

            # Try different lengths for current number
            for end in range(index + 1, len(s) + 1):
                # Don't take the entire remaining string on first number
                if count == 0 and end == len(s):
                    continue

                num = int(s[index:end])

                if count == 0 or num == prev - 1:
                    if backtrack(end, num, count + 1):
                        return True

            return False

        return backtrack(0, -1, 0)


class SolutionIterative:
    def splitString(self, s: str) -> bool:
        """
        Try each starting number, then verify sequence.
        """
        n = len(s)

        # Try each possible first number (can't use entire string)
        for first_len in range(1, n):
            first_num = int(s[:first_len])

            # Try to form descending sequence
            current = first_num
            idx = first_len
            count = 1

            while idx < n:
                target = current - 1
                target_str = str(target)

                # Check if next segment matches target
                if idx + len(target_str) <= n and \
                   int(s[idx:idx + len(target_str)]) == target:
                    idx += len(target_str)
                    current = target
                    count += 1
                else:
                    break

            if idx == n and count >= 2:
                return True

        return False


class SolutionDFS:
    def splitString(self, s: str) -> bool:
        """
        DFS with early termination.
        """
        def dfs(start: int, prev: int) -> bool:
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                num = int(s[start:end])

                # Prune: if num < prev - 1, no point continuing
                if num < prev - 1:
                    break

                if num == prev - 1:
                    if dfs(end, num):
                        return True

            return False

        # Try each first number length (excluding full string)
        for first_len in range(1, len(s)):
            first = int(s[:first_len])
            if dfs(first_len, first):
                return True

        return False
