#1593. Split a String Into the Max Number of Unique Substrings
#Medium
#
#Given a string s, return the maximum number of unique substrings that the
#given string can be split into.
#
#You can split string s into any list of non-empty substrings, where the
#concatenation of the substrings forms the original string. However, you must
#split the substrings such that all of them are unique.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: s = "ababccc"
#Output: 5
#Explanation: One way to split is ['a', 'b', 'ab', 'c', 'cc'].
#
#Example 2:
#Input: s = "aba"
#Output: 2
#Explanation: One way to split is ['a', 'ba'].
#
#Example 3:
#Input: s = "aa"
#Output: 1
#Explanation: It is impossible to split without repeated substrings.
#
#Constraints:
#    1 <= s.length <= 16
#    s contains only lower case English letters.

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        """
        Backtracking: Try all possible splits and track max unique count.
        """
        def backtrack(start: int, seen: set) -> int:
            if start == len(s):
                return 0

            max_count = 0

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring not in seen:
                    seen.add(substring)
                    max_count = max(max_count, 1 + backtrack(end, seen))
                    seen.remove(substring)

            return max_count

        return backtrack(0, set())


class SolutionOptimized:
    def maxUniqueSplit(self, s: str) -> int:
        """
        Backtracking with pruning.
        If remaining characters can't exceed current best, stop early.
        """
        self.max_count = 0
        n = len(s)

        def backtrack(start: int, seen: set):
            # Pruning: if we can't possibly beat the max, stop
            remaining = n - start
            if len(seen) + remaining <= self.max_count:
                return

            if start == n:
                self.max_count = max(self.max_count, len(seen))
                return

            for end in range(start + 1, n + 1):
                substring = s[start:end]

                if substring not in seen:
                    seen.add(substring)
                    backtrack(end, seen)
                    seen.remove(substring)

        backtrack(0, set())
        return self.max_count


class SolutionIterative:
    def maxUniqueSplit(self, s: str) -> int:
        """
        Iterative approach using stack for backtracking.
        """
        n = len(s)
        max_result = 1

        # Stack: (start_index, end_index, seen_set_copy)
        # Try starting with each possible first substring
        stack = []

        for end in range(1, n + 1):
            stack.append((0, end, {s[0:end]}))

        while stack:
            start, prev_end, seen = stack.pop()

            if prev_end == n:
                max_result = max(max_result, len(seen))
                continue

            # Pruning
            remaining = n - prev_end
            if len(seen) + remaining <= max_result:
                continue

            # Try all next substrings
            for end in range(prev_end + 1, n + 1):
                substring = s[prev_end:end]
                if substring not in seen:
                    new_seen = seen | {substring}
                    stack.append((prev_end, end, new_seen))

        return max_result


class SolutionBitmask:
    def maxUniqueSplit(self, s: str) -> int:
        """
        Use bitmask to represent split positions.
        For string of length n, there are n-1 possible split positions.
        """
        n = len(s)
        max_count = 1

        # Try all possible ways to place splits
        for mask in range(1 << (n - 1)):
            # Extract substrings based on split positions
            substrings = []
            start = 0

            for i in range(n - 1):
                if mask & (1 << i):
                    substrings.append(s[start:i + 1])
                    start = i + 1

            # Don't forget the last substring
            substrings.append(s[start:])

            # Check if all unique
            if len(substrings) == len(set(substrings)):
                max_count = max(max_count, len(substrings))

        return max_count
