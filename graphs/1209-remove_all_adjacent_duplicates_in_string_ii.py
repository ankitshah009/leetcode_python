#1209. Remove All Adjacent Duplicates in String II
#Medium
#
#You are given a string s and an integer k, a k duplicate removal consists of
#choosing k adjacent and equal letters from s and removing them, causing the
#left and the right side of the deleted substring to concatenate together.
#
#We repeatedly make k duplicate removals on s until we no longer can.
#
#Return the final string after all such duplicate removals have been made. It
#is guaranteed that the answer is unique.
#
#Example 1:
#Input: s = "abcd", k = 2
#Output: "abcd"
#Explanation: There's nothing to delete.
#
#Example 2:
#Input: s = "deeedbbcccbdaa", k = 3
#Output: "aa"
#Explanation:
#First delete "eee" and "ccc", get "ddbbbdaa"
#Then delete "bbb", get "dddaa"
#Finally delete "ddd", get "aa"
#
#Example 3:
#Input: s = "pbbcggttciiippooaais", k = 2
#Output: "ps"
#
#Constraints:
#    1 <= s.length <= 10^5
#    2 <= k <= 10^4
#    s only contains lowercase English letters.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Stack stores (char, count) pairs.
        When count reaches k, pop the entry.
        """
        stack = []  # [(char, count)]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])

        # Build result
        return ''.join(c * count for c, count in stack)


class SolutionTwoPointers:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Two pointers: build result in-place using array.
        """
        s = list(s)
        count = [0] * len(s)
        j = 0  # Write pointer

        for i in range(len(s)):
            s[j] = s[i]

            if j > 0 and s[j] == s[j - 1]:
                count[j] = count[j - 1] + 1
            else:
                count[j] = 1

            if count[j] == k:
                j -= k

            j += 1

        return ''.join(s[:j])


class SolutionRecursive:
    def removeDuplicates(self, s: str, k: int) -> str:
        """Recursive approach (less efficient)"""
        new_s = self._remove_once(s, k)
        while new_s != s:
            s = new_s
            new_s = self._remove_once(s, k)
        return s

    def _remove_once(self, s, k):
        result = []
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1

            count = j - i
            if count >= k:
                result.append(s[i] * (count % k))
            else:
                result.append(s[i:j])

            i = j

        return ''.join(result)
