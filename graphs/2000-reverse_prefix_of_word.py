#2000. Reverse Prefix of Word
#Easy
#
#Given a 0-indexed string word and a character ch, reverse the segment of word
#that starts at index 0 and ends at the index of the first occurrence of ch
#(inclusive). If the character ch does not exist in word, do nothing.
#
#For example, if word = "abcdefd" and ch = "d", then you should reverse the
#segment that starts at 0 and ends at 3 (inclusive). The resulting string will
#be "dcbaefd".
#
#Return the resulting string.
#
#Example 1:
#Input: word = "abcdefd", ch = "d"
#Output: "dcbaefd"
#Explanation: The first occurrence of "d" is at index 3.
#Reverse prefix from 0 to 3 (inclusive).
#
#Example 2:
#Input: word = "xyxzxe", ch = "z"
#Output: "zxyxxe"
#
#Example 3:
#Input: word = "abcd", ch = "z"
#Output: "abcd"
#Explanation: "z" does not exist in word. Return original string.
#
#Constraints:
#    1 <= word.length <= 250
#    word consists of lowercase English letters.
#    ch is a lowercase English letter.

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Find first occurrence and reverse prefix.
        """
        idx = word.find(ch)

        if idx == -1:
            return word

        return word[:idx + 1][::-1] + word[idx + 1:]


class SolutionExplicit:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Explicit loop to find character.
        """
        for i, c in enumerate(word):
            if c == ch:
                return word[:i + 1][::-1] + word[i + 1:]

        return word


class SolutionList:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Using list manipulation.
        """
        chars = list(word)

        try:
            idx = chars.index(ch)
        except ValueError:
            return word

        # Reverse prefix
        left, right = 0, idx
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return ''.join(chars)


class SolutionTwoPointer:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Two pointer approach.
        """
        # Find first occurrence
        idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break

        if idx == -1:
            return word

        # Convert to list and reverse
        result = list(word)
        left, right = 0, idx

        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

        return ''.join(result)
