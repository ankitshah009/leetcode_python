#1717. Maximum Score From Removing Substrings
#Medium
#
#You are given a string s and two integers x and y. You can perform two types
#of operations any number of times.
#
#- Remove substring "ab" and gain x points.
#- Remove substring "ba" and gain y points.
#
#Return the maximum points you can gain after applying the above operations on s.
#
#Example 1:
#Input: s = "cdbcbbaaabab", x = 4, y = 5
#Output: 19
#
#Example 2:
#Input: s = "aabbaaxybbaabb", x = 5, y = 4
#Output: 20
#
#Constraints:
#    1 <= s.length <= 10^5
#    1 <= x, y <= 10^4
#    s consists of lowercase English letters.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Greedy: remove higher-value pairs first.
        Use stack to efficiently remove pairs.
        """
        # Ensure we always try higher value first
        if x < y:
            # Swap to make "ab" the higher value pair
            x, y = y, x
            first, second = 'b', 'a'
        else:
            first, second = 'a', 'b'

        def remove_pair(s: str, c1: str, c2: str, points: int) -> tuple:
            """Remove all c1+c2 pairs and return remaining string and score."""
            stack = []
            score = 0

            for c in s:
                if stack and stack[-1] == c1 and c == c2:
                    stack.pop()
                    score += points
                else:
                    stack.append(c)

            return ''.join(stack), score

        # First pass: remove higher value pairs
        remaining, score1 = remove_pair(s, first, second, x)

        # Second pass: remove lower value pairs
        _, score2 = remove_pair(remaining, second, first, y)

        return score1 + score2


class SolutionCounting:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Count-based approach - process character by character.
        """
        if x < y:
            x, y = y, x
            first, second = 'b', 'a'
        else:
            first, second = 'a', 'b'

        total = 0
        first_count = 0
        second_count = 0

        for c in s + '#':  # Add sentinel to process last group
            if c == first:
                first_count += 1
            elif c == second:
                if first_count > 0:
                    # Form higher-value pair
                    total += x
                    first_count -= 1
                else:
                    second_count += 1
            else:
                # Different character - form remaining lower-value pairs
                pairs = min(first_count, second_count)
                total += pairs * y
                first_count = 0
                second_count = 0

        return total


class SolutionStack:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Single stack approach with two passes.
        """
        def process(chars: list, target: str, points: int) -> tuple:
            stack = []
            score = 0

            for c in chars:
                if len(target) == 2 and stack and stack[-1] == target[0] and c == target[1]:
                    stack.pop()
                    score += points
                else:
                    stack.append(c)

            return stack, score

        # Process higher value first
        if x >= y:
            remaining, score1 = process(list(s), "ab", x)
            _, score2 = process(remaining, "ba", y)
        else:
            remaining, score1 = process(list(s), "ba", y)
            _, score2 = process(remaining, "ab", x)

        return score1 + score2
