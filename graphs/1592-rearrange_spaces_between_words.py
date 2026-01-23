#1592. Rearrange Spaces Between Words
#Easy
#
#You are given a string text of words that are placed among some number of
#spaces. Each word consists of one or more lowercase English letters and are
#separated by at least one space. It's guaranteed that text contains at least
#one word.
#
#Rearrange the spaces so that there is an equal number of spaces between every
#pair of adjacent words and that number is maximized. If you cannot redistribute
#all the spaces equally, place the extra spaces at the end, meaning the returned
#string should be the same length as text.
#
#Return the string after rearranging the spaces.
#
#Example 1:
#Input: text = "  this   is  a sentence "
#Output: "this   is   a   sentence"
#Explanation: There are 9 spaces and 4 words. 9 // 3 = 3 spaces between words.
#
#Example 2:
#Input: text = " practice   makes   perfect"
#Output: "practice   makes   perfect "
#Explanation: 7 spaces and 3 words. 7 // 2 = 3 spaces, 1 extra space at end.
#
#Constraints:
#    1 <= text.length <= 100
#    text consists of lowercase English letters and ' '.
#    text contains at least one word.

class Solution:
    def reorderSpaces(self, text: str) -> str:
        """
        Count spaces and words, distribute evenly.
        """
        total_spaces = text.count(' ')
        words = text.split()

        if len(words) == 1:
            # Single word: all spaces at end
            return words[0] + ' ' * total_spaces

        # Calculate spaces between words
        gaps = len(words) - 1
        space_between = total_spaces // gaps
        extra_spaces = total_spaces % gaps

        result = (' ' * space_between).join(words)
        result += ' ' * extra_spaces

        return result


class SolutionDetailed:
    def reorderSpaces(self, text: str) -> str:
        """
        Step-by-step solution.
        """
        # Count total spaces
        space_count = sum(1 for c in text if c == ' ')

        # Extract words
        words = text.split()
        word_count = len(words)

        # Handle single word case
        if word_count == 1:
            return words[0] + ' ' * space_count

        # Calculate distribution
        num_gaps = word_count - 1
        spaces_per_gap = space_count // num_gaps
        remaining_spaces = space_count % num_gaps

        # Build result
        separator = ' ' * spaces_per_gap
        result = separator.join(words)

        # Add trailing spaces
        result += ' ' * remaining_spaces

        return result


class SolutionManual:
    def reorderSpaces(self, text: str) -> str:
        """
        Manual word extraction without split().
        """
        # Count spaces
        spaces = 0
        words = []
        current_word = []

        for c in text:
            if c == ' ':
                spaces += 1
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
            else:
                current_word.append(c)

        if current_word:
            words.append(''.join(current_word))

        # Distribute spaces
        n = len(words)

        if n == 1:
            return words[0] + ' ' * spaces

        between = spaces // (n - 1)
        trailing = spaces % (n - 1)

        parts = []
        for i, word in enumerate(words):
            parts.append(word)
            if i < n - 1:
                parts.append(' ' * between)

        parts.append(' ' * trailing)

        return ''.join(parts)
