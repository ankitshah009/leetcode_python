#1625. Lexicographically Smallest String After Applying Operations
#Medium
#
#You are given a string s of even length consisting of digits from 0 to 9, and
#two integers a and b.
#
#You can apply either of the following two operations any number of times and
#in any order on s:
#- Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0.
#- Rotate s to the right by b positions.
#
#Return the lexicographically smallest string you can obtain by applying the
#above operations any number of times on s.
#
#A string a is lexicographically smaller than a string b (of the same length)
#if in the first position where a and b differ, string a has a letter that
#appears earlier in the alphabet than the corresponding letter in b.
#
#Example 1:
#Input: s = "5525", a = 9, b = 2
#Output: "2050"
#Explanation: We can apply the following operations:
#Start: "5525"
#Rotate: "2555"
#Add: "2454"
#Add: "2353"
#Rotate: "5765"
#Add: "5765" -> "5765" (no change as adding 9 to 6 gives 15, and 15 mod 10 = 5)
#... (more operations to reach "2050")
#
#Example 2:
#Input: s = "74", a = 5, b = 1
#Output: "24"
#
#Example 3:
#Input: s = "0011", a = 4, b = 2
#Output: "0011"
#
#Constraints:
#    2 <= s.length <= 100
#    s.length is even.
#    s consists of digits from 0 to 9 only.
#    1 <= a <= 9
#    1 <= b <= s.length - 1

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        BFS/DFS to explore all possible states.
        Since string is bounded and operations are cyclic, we'll reach all states.
        """
        def add(string: str) -> str:
            chars = list(string)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            return ''.join(chars)

        def rotate(string: str) -> str:
            return string[-b:] + string[:-b]

        seen = set()
        smallest = s

        stack = [s]

        while stack:
            curr = stack.pop()

            if curr in seen:
                continue
            seen.add(curr)

            if curr < smallest:
                smallest = curr

            # Apply operations
            stack.append(add(curr))
            stack.append(rotate(curr))

        return smallest


class SolutionBFS:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        BFS approach for exploring states.
        """
        from collections import deque

        def add_op(string):
            return ''.join(
                str((int(c) + a) % 10) if i % 2 else c
                for i, c in enumerate(string)
            )

        def rotate_op(string):
            return string[-b:] + string[:-b]

        visited = {s}
        queue = deque([s])
        result = s

        while queue:
            curr = queue.popleft()
            result = min(result, curr)

            for next_s in [add_op(curr), rotate_op(curr)]:
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append(next_s)

        return result


class SolutionOptimized:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        Optimized: Consider all rotations and all add combinations.

        - Rotations: gcd(b, len(s)) determines unique positions
        - Add operations: cycle through 0-9 additions (10/gcd(10,a) unique values)
        """
        from math import gcd

        n = len(s)
        smallest = s

        # Generate all rotations
        rotations = []
        rot = s
        for _ in range(n // gcd(b, n)):
            rotations.append(rot)
            rot = rot[-b:] + rot[:-b]

        # For each rotation, try all add combinations
        add_cycles = 10 // gcd(10, a)

        for rot in rotations:
            chars = list(rot)

            # Apply add to odd indices
            for _ in range(add_cycles):
                # If b is odd, we can also modify even indices
                if b % 2 == 1:
                    for _ in range(add_cycles):
                        candidate = ''.join(chars)
                        smallest = min(smallest, candidate)
                        # Add to even indices
                        for i in range(0, n, 2):
                            chars[i] = str((int(chars[i]) + a) % 10)
                else:
                    candidate = ''.join(chars)
                    smallest = min(smallest, candidate)

                # Add to odd indices
                for i in range(1, n, 2):
                    chars[i] = str((int(chars[i]) + a) % 10)

        return smallest
