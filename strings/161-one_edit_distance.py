#161. One Edit Distance
#Medium
#
#Given two strings s and t, return true if they are both one edit distance apart,
#otherwise return false.
#
#A string s is said to be one distance apart from a string t if you can:
#- Insert exactly one character into s to get t.
#- Delete exactly one character from s to get t.
#- Replace exactly one character of s with a different character to get t.
#
#Example 1:
#Input: s = "ab", t = "acb"
#Output: true
#Explanation: We can insert 'c' into s to get t.
#
#Example 2:
#Input: s = "", t = ""
#Output: false
#Explanation: We cannot get t from s by only one step.
#
#Example 3:
#Input: s = "a", t = ""
#Output: true
#
#Constraints:
#    0 <= s.length, t.length <= 10^4
#    s and t consist of lowercase letters, uppercase letters, and digits.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # Ensure s is the shorter string
        if m > n:
            return self.isOneEditDistance(t, s)

        # Length difference must be at most 1
        if n - m > 1:
            return False

        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    # Replace: rest of strings must match
                    return s[i+1:] == t[i+1:]
                else:
                    # Insert/Delete: s[i:] must match t[i+1:]
                    return s[i:] == t[i+1:]

        # All characters matched, valid only if lengths differ by 1
        return m + 1 == n

    # Alternative explicit approach
    def isOneEditDistanceExplicit(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        if abs(m - n) > 1:
            return False

        if m == n:
            # Check for exactly one replacement
            diff_count = sum(1 for a, b in zip(s, t) if a != b)
            return diff_count == 1

        # Check for exactly one insertion/deletion
        if m > n:
            s, t = t, s  # Ensure s is shorter

        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i:] == t[i+1:]

        return True  # Difference is at the end
