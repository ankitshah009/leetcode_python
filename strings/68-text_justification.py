#68. Text Justification
#Hard
#
#Given an array of strings words and a width maxWidth, format the text such that each line
#has exactly maxWidth characters and is fully (left and right) justified.
#
#You should pack your words in a greedy approach; that is, pack as many words as you can
#in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
#Extra spaces between words should be distributed as evenly as possible. If the number of
#spaces on a line does not divide evenly between words, the empty slots on the left will be
#assigned more spaces than the slots on the right.
#
#For the last line of text, it should be left-justified, and no extra space is inserted
#between words.
#
#Example 1:
#Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
#Output:
#[
#   "This    is    an",
#   "example  of text",
#   "justification.  "
#]
#
#Example 2:
#Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
#Output:
#[
#  "What   must   be",
#  "acknowledgment  ",
#  "shall be        "
#]
#
#Constraints:
#    1 <= words.length <= 300
#    1 <= words[i].length <= 20
#    words[i] consists of only English letters and symbols.
#    1 <= maxWidth <= 100
#    words[i].length <= maxWidth

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0

        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                # Justify current line
                spaces_needed = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces_needed)
                else:
                    gaps = len(line) - 1
                    space_per_gap = spaces_needed // gaps
                    extra_spaces = spaces_needed % gaps

                    justified_line = ""
                    for i, w in enumerate(line[:-1]):
                        justified_line += w + ' ' * space_per_gap
                        if i < extra_spaces:
                            justified_line += ' '
                    justified_line += line[-1]
                    result.append(justified_line)

                line = []
                line_length = 0

            line.append(word)
            line_length += len(word)

        # Last line - left justified
        last_line = ' '.join(line)
        result.append(last_line + ' ' * (maxWidth - len(last_line)))

        return result
