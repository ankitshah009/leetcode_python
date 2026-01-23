#1678. Goal Parser Interpretation
#Easy
#
#You own a Goal Parser that can interpret a string command. The command consists
#of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will
#interpret "G" as the string "G", "()" as the string "o", and "(al)" as the
#string "al". The interpreted strings are then concatenated in the original order.
#
#Given the string command, return the Goal Parser's interpretation of command.
#
#Example 1:
#Input: command = "G()(al)"
#Output: "Goal"
#Explanation: The Goal Parser interprets the command as follows:
#G -> G, () -> o, (al) -> al. Concatenated: "Goal"
#
#Example 2:
#Input: command = "G()()()()(al)"
#Output: "Gooooal"
#
#Example 3:
#Input: command = "(al)G(al)()()G"
#Output: "alGalooG"
#
#Constraints:
#    1 <= command.length <= 100
#    command consists of "G", "()", and/or "(al)" in some order.

class Solution:
    def interpret(self, command: str) -> str:
        """
        Simple string replacement.
        """
        return command.replace("()", "o").replace("(al)", "al")


class SolutionParsing:
    def interpret(self, command: str) -> str:
        """
        Character-by-character parsing.
        """
        result = []
        i = 0

        while i < len(command):
            if command[i] == 'G':
                result.append('G')
                i += 1
            elif command[i:i+2] == '()':
                result.append('o')
                i += 2
            elif command[i:i+4] == '(al)':
                result.append('al')
                i += 4

        return ''.join(result)


class SolutionStateMachine:
    def interpret(self, command: str) -> str:
        """
        State machine approach.
        """
        result = []
        i = 0

        while i < len(command):
            c = command[i]

            if c == 'G':
                result.append('G')
                i += 1
            elif c == '(':
                if i + 1 < len(command) and command[i + 1] == ')':
                    result.append('o')
                    i += 2
                else:
                    # Must be (al)
                    result.append('al')
                    i += 4

        return ''.join(result)


class SolutionRegex:
    def interpret(self, command: str) -> str:
        """
        Using regex for replacement.
        """
        import re
        result = re.sub(r'\(\)', 'o', command)
        result = re.sub(r'\(al\)', 'al', result)
        return result


class SolutionCompact:
    def interpret(self, command: str) -> str:
        """
        One-liner solution.
        """
        return command.replace("()", "o").replace("(al)", "al")
