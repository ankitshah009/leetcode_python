#1805. Number of Different Integers in a String
#Easy
#
#You are given a string word that consists of digits and lowercase English
#letters.
#
#You will replace every non-digit character with a space. For example,
#"a]123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with
#some integers that are separated by at least one space: "123", "34", "8", and
#"34".
#
#Return the number of different integers after performing the replacement
#operations on word.
#
#Two integers are considered different if their decimal representations without
#any leading zeros are different.
#
#Example 1:
#Input: word = "a123bc34d8ef34"
#Output: 3
#
#Example 2:
#Input: word = "leet1234code234"
#Output: 2
#
#Example 3:
#Input: word = "a1b01c001"
#Output: 1
#
#Constraints:
#    1 <= word.length <= 1000
#    word consists of digits and lowercase English letters.

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        """
        Extract integers and normalize (remove leading zeros).
        """
        # Replace non-digits with spaces
        s = ''.join(c if c.isdigit() else ' ' for c in word)

        # Split and remove leading zeros
        integers = set()
        for part in s.split():
            # Remove leading zeros by converting to int and back
            integers.add(str(int(part)))

        return len(integers)


class SolutionManual:
    def numDifferentIntegers(self, word: str) -> int:
        """
        Manual extraction without replace.
        """
        integers = set()
        i = 0
        n = len(word)

        while i < n:
            if word[i].isdigit():
                # Skip leading zeros
                while i < n and word[i] == '0':
                    i += 1

                # Collect remaining digits
                num = []
                while i < n and word[i].isdigit():
                    num.append(word[i])
                    i += 1

                # Empty means it was all zeros
                integers.add(''.join(num) if num else '0')
            else:
                i += 1

        return len(integers)


class SolutionRegex:
    def numDifferentIntegers(self, word: str) -> int:
        """
        Using regex to find all integers.
        """
        import re
        numbers = re.findall(r'\d+', word)
        # Normalize by removing leading zeros
        return len(set(n.lstrip('0') or '0' for n in numbers))
