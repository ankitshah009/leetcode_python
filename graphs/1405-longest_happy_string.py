#1405. Longest Happy String
#Medium
#
#A string s is called happy if it satisfies the following conditions:
#    s only contains the letters 'a', 'b', and 'c'.
#    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
#    s contains at most a occurrences of the letter 'a'.
#    s contains at most b occurrences of the letter 'b'.
#    s contains at most c occurrences of the letter 'c'.
#
#Given three integers a, b, and c, return the longest possible happy string.
#If there are multiple longest happy strings, return any of them. If there is
#no such string, return the empty string "".
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: a = 1, b = 1, c = 7
#Output: "ccaccbcc"
#Explanation: "ccbccacc" would also be a correct answer.
#
#Example 2:
#Input: a = 7, b = 1, c = 0
#Output: "aabaa"
#Explanation: It is the only correct answer in this case.
#
#Constraints:
#    0 <= a, b, c <= 100
#    a + b + c > 0

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Greedy with max heap:
        Always try to use the character with most remaining count.
        If it would create 3 in a row, use second most.
        """
        # Max heap: (-count, char)
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        result = []

        while heap:
            count1, char1 = heapq.heappop(heap)

            # Check if adding char1 creates "xxx"
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                # Need to use second character instead
                if not heap:
                    break  # No other option

                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                count2 += 1  # Used one

                if count2 < 0:
                    heapq.heappush(heap, (count2, char2))

                # Put first back
                heapq.heappush(heap, (count1, char1))
            else:
                result.append(char1)
                count1 += 1  # Used one (count is negative)

                if count1 < 0:
                    heapq.heappush(heap, (count1, char1))

        return ''.join(result)


class SolutionIterative:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """Iterative without heap"""
        result = []
        counts = [a, b, c]
        chars = ['a', 'b', 'c']

        while True:
            # Sort by count descending
            order = sorted(range(3), key=lambda i: -counts[i])

            added = False
            for i in order:
                if counts[i] == 0:
                    continue

                # Check if we can add this character
                n = len(result)
                if n >= 2 and result[-1] == chars[i] and result[-2] == chars[i]:
                    continue

                result.append(chars[i])
                counts[i] -= 1
                added = True
                break

            if not added:
                break

        return ''.join(result)


class SolutionGreedy:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Greedy: always add from max available.
        Add 2 if much larger than others, else add 1.
        """
        result = []

        def get_sorted():
            return sorted([('a', a), ('b', b), ('c', c)], key=lambda x: -x[1])

        while True:
            sorted_chars = sorted([('a', a), ('b', b), ('c', c)],
                                  key=lambda x: -x[1])

            for char, count in sorted_chars:
                if count == 0:
                    continue

                n = len(result)
                if n >= 2 and result[-1] == char and result[-2] == char:
                    continue

                result.append(char)

                # Update count
                if char == 'a':
                    a -= 1
                elif char == 'b':
                    b -= 1
                else:
                    c -= 1

                break
            else:
                # No character could be added
                break

        return ''.join(result)
