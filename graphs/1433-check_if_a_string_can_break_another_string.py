#1433. Check If a String Can Break Another String
#Medium
#
#Given two strings: s1 and s2 with the same size, check if some permutation of
#string s1 can break some permutation of string s2 or vice-versa. In other words
#s2 can break s1 or vice-versa.
#
#A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical
#order) for all i between 0 and n-1.
#
#Example 1:
#Input: s1 = "abc", s2 = "xya"
#Output: true
#Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc"
#which is a permutation of s1="abc".
#
#Example 2:
#Input: s1 = "abe", s2 = "acd"
#Output: false
#Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea",
#"eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad",
#"cda", "dac" and "dca". However, there is not any permutation from s1 which
#can break some permutation from s2 and vice-versa.
#
#Example 3:
#Input: s1 = "leetcodee", s2 = "interview"
#Output: true
#
#Constraints:
#    s1.length == n
#    s2.length == n
#    1 <= n <= 10^5
#    All strings consist of lowercase English letters.

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """
        Sort both strings. Then either:
        - sorted(s1)[i] >= sorted(s2)[i] for all i, or
        - sorted(s2)[i] >= sorted(s1)[i] for all i
        """
        sorted1 = sorted(s1)
        sorted2 = sorted(s2)

        # Check if s1 can break s2
        can_s1_break_s2 = all(c1 >= c2 for c1, c2 in zip(sorted1, sorted2))

        # Check if s2 can break s1
        can_s2_break_s1 = all(c2 >= c1 for c1, c2 in zip(sorted1, sorted2))

        return can_s1_break_s2 or can_s2_break_s1


class SolutionExplicit:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """More explicit version"""
        sorted1 = sorted(s1)
        sorted2 = sorted(s2)
        n = len(s1)

        # Check if sorted1 can break sorted2
        s1_breaks = True
        s2_breaks = True

        for i in range(n):
            if sorted1[i] < sorted2[i]:
                s1_breaks = False
            if sorted2[i] < sorted1[i]:
                s2_breaks = False

        return s1_breaks or s2_breaks


class SolutionCounting:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """Using character counting"""
        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord('a')] += 1
        for c in s2:
            count2[ord(c) - ord('a')] += 1

        # Check if count1 can "dominate" count2 or vice versa
        # cumulative count comparison
        cum1 = cum2 = 0
        can_1_break = can_2_break = True

        for i in range(26):
            cum1 += count1[i]
            cum2 += count2[i]

            # For s1 to break s2, at each point cum1 should have "smaller" chars
            if cum1 > cum2:
                can_1_break = False
            if cum2 > cum1:
                can_2_break = False

        return can_1_break or can_2_break
