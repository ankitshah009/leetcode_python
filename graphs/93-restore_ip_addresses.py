#93. Restore IP Addresses
#Medium
#
#A valid IP address consists of exactly four integers separated by single dots.
#Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#
#Given a string s containing only digits, return all possible valid IP addresses
#that can be formed by inserting dots into s. You are not allowed to reorder or
#remove any digits in s.
#
#Example 1:
#Input: s = "25525511135"
#Output: ["255.255.11.135","255.255.111.35"]
#
#Example 2:
#Input: s = "0000"
#Output: ["0.0.0.0"]
#
#Example 3:
#Input: s = "101023"
#Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#Constraints:
#    1 <= s.length <= 20
#    s consists of digits only.

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Backtracking approach.
        """
        result = []

        def is_valid(segment: str) -> bool:
            if not segment:
                return False
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255

        def backtrack(start: int, parts: List[str]):
            if len(parts) == 4:
                if start == len(s):
                    result.append('.'.join(parts))
                return

            # Remaining characters check
            remaining = len(s) - start
            parts_needed = 4 - len(parts)

            if remaining < parts_needed or remaining > parts_needed * 3:
                return

            # Try segments of length 1, 2, 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start:start + length]
                if is_valid(segment):
                    backtrack(start + length, parts + [segment])

        backtrack(0, [])
        return result


class SolutionIterative:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Three nested loops for three dots.
        """
        result = []
        n = len(s)

        def is_valid(segment: str) -> bool:
            if not segment or len(segment) > 3:
                return False
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255

        for i in range(1, min(4, n)):
            for j in range(i + 1, min(i + 4, n)):
                for k in range(j + 1, min(j + 4, n)):
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]

                    if all(is_valid(seg) for seg in [s1, s2, s3, s4]):
                        result.append(f"{s1}.{s2}.{s3}.{s4}")

        return result


class SolutionDFS:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        DFS with explicit pruning.
        """
        result = []
        n = len(s)

        def dfs(index: int, dots: int, current: str):
            if dots == 4:
                if index == n:
                    result.append(current[:-1])  # Remove trailing dot
                return

            # Maximum 3 digits per segment
            for i in range(1, 4):
                if index + i > n:
                    break

                segment = s[index:index + i]

                # Validation
                if len(segment) > 1 and segment[0] == '0':
                    continue
                if int(segment) > 255:
                    continue

                dfs(index + i, dots + 1, current + segment + '.')

        dfs(0, 0, '')
        return result


class SolutionBruteForce:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Generate all possibilities and filter.
        """
        result = []
        n = len(s)

        if n < 4 or n > 12:
            return result

        def is_valid_ip(parts: List[str]) -> bool:
            for part in parts:
                if not part:
                    return False
                if len(part) > 1 and part[0] == '0':
                    return False
                if int(part) > 255:
                    return False
            return True

        # Try all combinations of 3 dots
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    d = n - a - b - c
                    if 1 <= d <= 3:
                        parts = [s[:a], s[a:a+b], s[a+b:a+b+c], s[a+b+c:]]
                        if is_valid_ip(parts):
                            result.append('.'.join(parts))

        return result
