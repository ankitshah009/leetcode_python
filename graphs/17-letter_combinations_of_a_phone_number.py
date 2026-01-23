#17. Letter Combinations of a Phone Number
#Medium
#
#Given a string containing digits from 2-9 inclusive, return all possible letter
#combinations that the number could represent. Return the answer in any order.
#
#A mapping of digits to letters (just like on the telephone buttons):
#2 -> abc, 3 -> def, 4 -> ghi, 5 -> jkl, 6 -> mno, 7 -> pqrs, 8 -> tuv, 9 -> wxyz
#
#Example 1:
#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#Example 2:
#Input: digits = ""
#Output: []
#
#Example 3:
#Input: digits = "2"
#Output: ["a","b","c"]
#
#Constraints:
#    0 <= digits.length <= 4
#    digits[i] is a digit in the range ['2', '9'].

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Backtracking approach.
        """
        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(index: int, current: str):
            if index == len(digits):
                result.append(current)
                return

            for letter in phone_map[digits[index]]:
                backtrack(index + 1, current + letter)

        backtrack(0, "")
        return result


class SolutionIterative:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Iterative BFS-like approach.
        """
        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = ['']

        for digit in digits:
            new_result = []
            for combination in result:
                for letter in phone_map[digit]:
                    new_result.append(combination + letter)
            result = new_result

        return result


class SolutionProduct:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Using itertools.product.
        """
        from itertools import product

        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        letters = [phone_map[d] for d in digits]
        return [''.join(combo) for combo in product(*letters)]


class SolutionReduce:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Using reduce for functional approach.
        """
        from functools import reduce

        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        return reduce(
            lambda acc, digit: [x + y for x in acc for y in phone_map[digit]],
            digits,
            ['']
        )
