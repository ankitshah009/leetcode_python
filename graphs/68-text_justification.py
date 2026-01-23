#68. Text Justification
#Hard
#
#Given an array of strings words and a width maxWidth, format the text such that
#each line has exactly maxWidth characters and is fully (left and right) justified.
#
#You should pack your words in a greedy approach; that is, pack as many words as
#you can in each line. Pad extra spaces ' ' when necessary so that each line has
#exactly maxWidth characters.
#
#Extra spaces between words should be distributed as evenly as possible. If the
#number of spaces on a line does not divide evenly between words, the empty slots
#on the left will be assigned more spaces than the slots on the right.
#
#For the last line of text, it should be left-justified, and no extra space is
#inserted between words.
#
#Example 1:
#Input: words = ["This", "is", "an", "example", "of", "text", "justification."],
#maxWidth = 16
#Output:
#[
#   "This    is    an",
#   "example  of text",
#   "justification.  "
#]
#
#Constraints:
#    1 <= words.length <= 300
#    1 <= words[i].length <= 20
#    words[i] consists of only English letters and symbols.
#    1 <= maxWidth <= 100
#    words[i].length <= maxWidth

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Greedy line packing with even space distribution.
        """
        result = []
        line = []
        line_length = 0

        for word in words:
            # Check if word fits in current line
            if line_length + len(word) + len(line) > maxWidth:
                # Justify current line
                result.append(self.justify(line, maxWidth, line_length))
                line = []
                line_length = 0

            line.append(word)
            line_length += len(word)

        # Last line - left justified
        last_line = ' '.join(line)
        result.append(last_line + ' ' * (maxWidth - len(last_line)))

        return result

    def justify(self, words: List[str], maxWidth: int, words_length: int) -> str:
        """
        Justify a line of words.
        """
        if len(words) == 1:
            return words[0] + ' ' * (maxWidth - len(words[0]))

        total_spaces = maxWidth - words_length
        gaps = len(words) - 1

        space_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps

        result = []
        for i, word in enumerate(words[:-1]):
            result.append(word)
            spaces = space_per_gap + (1 if i < extra_spaces else 0)
            result.append(' ' * spaces)

        result.append(words[-1])
        return ''.join(result)


class SolutionSimple:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Simplified approach.
        """
        result = []
        i = 0

        while i < len(words):
            # Find words that fit in current line
            line_words = []
            line_len = 0

            while i < len(words):
                word_len = len(words[i])
                if line_len + word_len + len(line_words) <= maxWidth:
                    line_words.append(words[i])
                    line_len += word_len
                    i += 1
                else:
                    break

            # Build line
            if i == len(words) or len(line_words) == 1:
                # Last line or single word - left justify
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                # Distribute spaces evenly
                spaces_needed = maxWidth - line_len
                gaps = len(line_words) - 1
                base_spaces = spaces_needed // gaps
                extra = spaces_needed % gaps

                line = ''
                for j, word in enumerate(line_words[:-1]):
                    spaces = base_spaces + (1 if j < extra else 0)
                    line += word + ' ' * spaces
                line += line_words[-1]

            result.append(line)

        return result
