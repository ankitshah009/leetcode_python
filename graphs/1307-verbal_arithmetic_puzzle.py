#1307. Verbal Arithmetic Puzzle
#Hard
#
#Given an equation, represented by words on the left side and the result on the
#right side.
#
#You need to check if the equation is solvable under the following rules:
#    Each character is decoded as one digit (0 - 9).
#    No two characters can map to the same digit.
#    Each words[i] and result are decoded as one number without leading zeros.
#    Sum of numbers on the left side (words) will equal to the number on the
#    right side (result).
#
#Return true if the equation is solvable, otherwise return false.
#
#Example 1:
#Input: words = ["SEND","MORE"], result = "MONEY"
#Output: true
#Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->2
#Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
#
#Example 2:
#Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
#Output: true
#Explanation: Map 'S'->6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->3, 'Y'->4
#
#Example 3:
#Input: words = ["LEET","CODE"], result = "POINT"
#Output: false
#
#Constraints:
#    2 <= words.length <= 5
#    1 <= words[i].length, result.length <= 7
#    words[i], result contain only uppercase English letters.
#    The number of different characters used in the expression is at most 10.

from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        """
        Backtracking with pruning.
        Process column by column from right to left.
        """
        # Get all unique characters
        all_chars = set(''.join(words) + result)
        chars = list(all_chars)

        # Characters that can't be 0 (leading digits)
        non_zero = set()
        for word in words:
            if len(word) > 1:
                non_zero.add(word[0])
        if len(result) > 1:
            non_zero.add(result[0])

        # Early termination: result can't be shorter than longest word
        max_len = max(len(w) for w in words)
        if len(result) < max_len:
            return False

        # Mapping
        char_to_digit = {}
        used_digits = [False] * 10

        def word_value(word):
            """Convert word to number using current mapping"""
            val = 0
            for c in word:
                val = val * 10 + char_to_digit[c]
            return val

        def backtrack(idx):
            if idx == len(chars):
                # Check if equation holds
                total = sum(word_value(w) for w in words)
                return total == word_value(result)

            char = chars[idx]
            start = 1 if char in non_zero else 0

            for digit in range(start, 10):
                if not used_digits[digit]:
                    char_to_digit[char] = digit
                    used_digits[digit] = True

                    if backtrack(idx + 1):
                        return True

                    del char_to_digit[char]
                    used_digits[digit] = False

            return False

        return backtrack(0)


class SolutionColumnWise:
    def isSolvable(self, words: List[str], result: str) -> bool:
        """Process column by column with carry for better pruning"""
        # Reverse all words for easier column processing
        words = [w[::-1] for w in words]
        result = result[::-1]

        max_len = max(max(len(w) for w in words), len(result))

        # Pad words with '#' (placeholder)
        words = [w.ljust(max_len, '#') for w in words]
        result = result.ljust(max_len, '#')

        # Characters that can't be zero
        non_zero = set()
        for w in words:
            if w[-1] != '#':
                non_zero.add(w[-1])
        if result[-1] != '#':
            non_zero.add(result[-1])

        char_to_digit = {'#': 0}
        used = {0}

        def solve(col, idx, carry):
            # Finished all columns
            if col == max_len:
                return carry == 0

            # Finished current column
            if idx == len(words):
                total = sum(char_to_digit[w[col]] for w in words) + carry
                digit = total % 10
                new_carry = total // 10

                res_char = result[col]
                if res_char in char_to_digit:
                    if char_to_digit[res_char] != digit:
                        return False
                    return solve(col + 1, 0, new_carry)
                else:
                    if digit in used or (digit == 0 and res_char in non_zero):
                        return False
                    char_to_digit[res_char] = digit
                    used.add(digit)
                    if solve(col + 1, 0, new_carry):
                        return True
                    del char_to_digit[res_char]
                    used.remove(digit)
                    return False

            # Process character at words[idx][col]
            char = words[idx][col]
            if char in char_to_digit:
                return solve(col, idx + 1, carry)

            start = 1 if char in non_zero else 0
            for digit in range(start, 10):
                if digit not in used:
                    char_to_digit[char] = digit
                    used.add(digit)
                    if solve(col, idx + 1, carry):
                        return True
                    del char_to_digit[char]
                    used.remove(digit)

            return False

        return solve(0, 0, 0)
