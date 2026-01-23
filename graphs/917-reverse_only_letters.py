#917. Reverse Only Letters
#Easy
#
#Given a string s, reverse the string according to the following rules:
#- All the characters that are not English letters remain in the same position.
#- All the English letters (lowercase or uppercase) should be reversed.
#
#Return s after reversing it.
#
#Example 1:
#Input: s = "ab-cd"
#Output: "dc-ba"
#
#Example 2:
#Input: s = "a-bC-dEf-ghIj"
#Output: "j-Ih-gfE-dCba"
#
#Example 3:
#Input: s = "Test1ng-Leet=code-Q!"
#Output: "Qedo1teleC-tset=LeeT-t!"
#
#Constraints:
#    1 <= s.length <= 100
#    s consists of characters with ASCII values in the range [33, 122].
#    s does not contain '\"' or '\\'.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Two pointer approach.
        """
        chars = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if not chars[left].isalpha():
                left += 1
            elif not chars[right].isalpha():
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return ''.join(chars)


class SolutionStack:
    """Using stack for letters"""

    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        result = []

        for c in s:
            if c.isalpha():
                result.append(letters.pop())
            else:
                result.append(c)

        return ''.join(result)


class SolutionReverse:
    """Extract, reverse, put back"""

    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()][::-1]
        result = []
        letter_idx = 0

        for c in s:
            if c.isalpha():
                result.append(letters[letter_idx])
                letter_idx += 1
            else:
                result.append(c)

        return ''.join(result)
