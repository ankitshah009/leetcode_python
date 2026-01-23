#1963. Minimum Number of Swaps to Make the String Balanced
#Medium
#
#You are given a 0-indexed string s of even length n. The string consists of
#exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
#
#A string is called balanced if and only if:
#- It is the empty string, or
#- It can be written as AB, where both A and B are balanced strings, or
#- It can be written as [C], where C is a balanced string.
#
#You may swap the brackets at any two indices any number of times.
#
#Return the minimum number of swaps to make s balanced.
#
#Example 1:
#Input: s = "][]["
#Output: 1
#Explanation: Swap index 0 with index 3. s = "[[]]".
#
#Example 2:
#Input: s = "]]][[["
#Output: 2
#
#Example 3:
#Input: s = "[]"
#Output: 0
#
#Constraints:
#    n == s.length
#    2 <= n <= 10^6
#    n is even.
#    s[i] is either '[' or ']'.
#    The number of opening brackets '[' equals n / 2.
#    The number of closing brackets ']' equals n / 2.

class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Count unmatched closing brackets.
        Each swap fixes 2 unmatched pairs.
        """
        unmatched = 0  # Unmatched ']' count

        for c in s:
            if c == '[':
                # Can match a previous unmatched ']'
                if unmatched > 0:
                    unmatched -= 1
            else:  # c == ']'
                unmatched += 1

        # Each swap fixes 2 unmatched pairs
        return (unmatched + 1) // 2


class SolutionStack:
    def minSwaps(self, s: str) -> int:
        """
        Use stack to simulate matching.
        """
        stack = []

        for c in s:
            if c == '[':
                stack.append(c)
            elif stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)

        # Stack has unmatched brackets in pattern "]]]...[[[..."
        # Number of unmatched pairs = len(stack) // 2
        unmatched_pairs = len(stack) // 2

        # Each swap fixes 2 pairs
        return (unmatched_pairs + 1) // 2


class SolutionCounting:
    def minSwaps(self, s: str) -> int:
        """
        Track balance and count maximum imbalance.
        """
        balance = 0
        max_imbalance = 0

        for c in s:
            if c == '[':
                balance += 1
            else:
                balance -= 1
                max_imbalance = max(max_imbalance, -balance)

        # Each swap reduces imbalance by 2
        return (max_imbalance + 1) // 2
