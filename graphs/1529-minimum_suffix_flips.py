#1529. Minimum Suffix Flips
#Medium
#
#You are given a 0-indexed binary string target of length n. You have another
#binary string s of length n that is initially set to all zeros. You want to
#make s equal to target.
#
#In one operation, you can pick an index i where 0 <= i < n and flip all bits
#in the inclusive range [i, n - 1]. Flip means changing '0' to '1' and '1' to '0'.
#
#Return the minimum number of operations needed to make s equal to target.
#
#Example 1:
#Input: target = "10111"
#Output: 3
#Explanation: Initially, s = "00000".
#Choose index i = 2: "00000" -> "00111"
#Choose index i = 0: "00111" -> "11000"
#Choose index i = 1: "11000" -> "10111"
#
#Example 2:
#Input: target = "101"
#Output: 3
#Explanation: Initially, s = "00000".
#Choose index i = 0: "000" -> "111"
#Choose index i = 1: "111" -> "100"
#Choose index i = 2: "100" -> "101"
#
#Example 3:
#Input: target = "00000"
#Output: 0
#Explanation: We don't need any operations since the initial s already equals target.
#
#Constraints:
#    n == target.length
#    1 <= n <= 10^5
#    target[i] is either '0' or '1'.

class Solution:
    def minFlips(self, target: str) -> int:
        """
        Count the number of times the target changes from 0 to 1 or 1 to 0.
        Each change requires a flip operation.

        Start with all 0s. Each time target[i] differs from target[i-1]
        (or from 0 at the start), we need one flip.
        """
        flips = 0
        current = '0'

        for char in target:
            if char != current:
                flips += 1
                current = char

        return flips


class SolutionExplicit:
    def minFlips(self, target: str) -> int:
        """
        More explicit: count transitions.
        """
        if not target:
            return 0

        # First char: if '1', need to flip from '0'
        flips = 1 if target[0] == '1' else 0

        # Count transitions
        for i in range(1, len(target)):
            if target[i] != target[i - 1]:
                flips += 1

        return flips


class SolutionGroup:
    def minFlips(self, target: str) -> int:
        """
        Count groups of consecutive same characters.
        Each '1' group needs a flip to create, each '0' group after a '1' needs a flip too.
        """
        from itertools import groupby

        groups = [(char, sum(1 for _ in g)) for char, g in groupby(target)]

        # Count '1' groups (need to flip on)
        # and subsequent '0' groups after '1' (need to flip off)
        flips = 0
        seen_one = False

        for char, _ in groups:
            if char == '1':
                flips += 1
                seen_one = True
            elif seen_one:  # '0' after a '1' group
                flips += 1

        return flips


class SolutionZip:
    def minFlips(self, target: str) -> int:
        """Using zip to count transitions"""
        # Prepend '0' (initial state)
        extended = '0' + target

        # Count transitions
        return sum(1 for a, b in zip(extended, extended[1:]) if a != b)


class SolutionReduce:
    def minFlips(self, target: str) -> int:
        """Using reduce"""
        from functools import reduce

        def count_flips(state, char):
            current, flips = state
            if char != current:
                return (char, flips + 1)
            return state

        _, flips = reduce(count_flips, target, ('0', 0))
        return flips
