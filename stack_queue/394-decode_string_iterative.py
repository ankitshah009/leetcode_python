#394. Decode String (Alternative iterative solution)
#Medium
#
#Given an encoded string, return its decoded string.
#
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
#is being repeated exactly k times.
#
#This file contains an alternative iterative implementation.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current state to stack
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == ']':
                # Pop and build string
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char

        return current_str
