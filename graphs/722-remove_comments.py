#722. Remove Comments
#Medium
#
#Given a C++ program, remove comments from it. The program source is an array
#of strings source where source[i] is the ith line of the source code.
#
#We will remove any characters from // to the end of that line.
#We will remove any characters between /* and */, including any line breaks.
#
#If at the end a line is empty, you should not output that line.
#
#Example 1:
#Input: source = ["/*Test program */", "int main()", "{ ",
#                 "  // variable declaration ", "int a, b, c;",
#                 "/* This is a test", "   multiline  ", "   comment for ",
#                 "   testing */", "a = b + c;", "}"]
#Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
#
#Example 2:
#Input: source = ["a/*comment", "line", "more_comment*/b"]
#Output: ["ab"]
#
#Constraints:
#    1 <= source.length <= 100
#    0 <= source[i].length <= 80
#    source[i] consists of printable ASCII characters.

class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        """
        State machine: track if inside block comment.
        """
        result = []
        in_block = False
        current_line = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    # Look for end of block comment
                    if i + 1 < len(line) and line[i:i+2] == '*/':
                        in_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    # Check for start of comments
                    if i + 1 < len(line) and line[i:i+2] == '/*':
                        in_block = True
                        i += 2
                    elif i + 1 < len(line) and line[i:i+2] == '//':
                        break  # Skip rest of line
                    else:
                        current_line.append(line[i])
                        i += 1

            # End of line processing
            if not in_block and current_line:
                result.append(''.join(current_line))
                current_line = []

        return result


class SolutionRegex:
    """Using regex for comment removal"""

    def removeComments(self, source: list[str]) -> list[str]:
        import re

        # Join all lines with newlines
        code = '\n'.join(source)

        # Remove block comments (non-greedy)
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)

        # Remove line comments
        code = re.sub(r'//[^\n]*', '', code)

        # Split back to lines and filter empty
        return [line for line in code.split('\n') if line]


class SolutionExplicit:
    """More explicit state handling"""

    def removeComments(self, source: list[str]) -> list[str]:
        result = []
        buffer = []
        in_block_comment = False

        for line in source:
            i = 0
            n = len(line)

            while i < n:
                c = line[i]
                next_c = line[i + 1] if i + 1 < n else ''

                if in_block_comment:
                    if c == '*' and next_c == '/':
                        in_block_comment = False
                        i += 1  # Skip '/'
                else:
                    if c == '/' and next_c == '*':
                        in_block_comment = True
                        i += 1  # Skip '*'
                    elif c == '/' and next_c == '/':
                        break  # Rest of line is comment
                    else:
                        buffer.append(c)

                i += 1

            # If not in block comment, flush buffer to result
            if not in_block_comment:
                if buffer:
                    result.append(''.join(buffer))
                buffer = []

        return result
