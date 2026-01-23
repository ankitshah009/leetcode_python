#942. DI String Match
#Easy
#
#A permutation perm of n + 1 integers of all the integers in the range [0, n]
#can be represented as a string s of length n where:
#- s[i] == 'I' if perm[i] < perm[i + 1], and
#- s[i] == 'D' if perm[i] > perm[i + 1].
#
#Given a string s, reconstruct the permutation perm and return it. If there are
#multiple valid permutations, return any of them.
#
#Example 1:
#Input: s = "IDID"
#Output: [0,4,1,3,2]
#
#Example 2:
#Input: s = "III"
#Output: [0,1,2,3]
#
#Example 3:
#Input: s = "DDI"
#Output: [3,2,0,1]
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is either 'I' or 'D'.

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        """
        Greedy: for 'I' use smallest available, for 'D' use largest.
        """
        n = len(s)
        low, high = 0, n
        result = []

        for c in s:
            if c == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        result.append(low)  # low == high at this point
        return result


class SolutionExplicit:
    """With explicit tracking"""

    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        result = [0] * (n + 1)
        low, high = 0, n

        for i, c in enumerate(s):
            if c == 'I':
                result[i] = low
                low += 1
            else:
                result[i] = high
                high -= 1

        result[n] = low
        return result


class SolutionStack:
    """Using stack for consecutive D's"""

    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        result = []
        stack = []

        for i in range(n + 1):
            stack.append(i)
            if i == n or s[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return result
