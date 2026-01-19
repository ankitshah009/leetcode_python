#394. Decode String
#Medium
#
#Given an encoded string, return its decoded string.
#
#The encoding rule is: k[encoded_string], where the encoded_string inside the
#square brackets is being repeated exactly k times. Note that k is guaranteed
#to be a positive integer.
#
#You may assume that the input string is always valid; there are no extra white
#spaces, square brackets are well-formed, etc. Furthermore, you may assume that
#the original data does not contain any digits and that digits are only for
#those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
#The test cases are generated so that the length of the output will never
#exceed 10^5.
#
#Example 1:
#Input: s = "3[a]2[bc]"
#Output: "aaabcbc"
#
#Example 2:
#Input: s = "3[a2[c]]"
#Output: "accaccacc"
#
#Example 3:
#Input: s = "2[abc]3[cd]ef"
#Output: "abcabccdcdcdef"
#
#Constraints:
#    1 <= s.length <= 30
#    s consists of lowercase English letters, digits, and square brackets '[]'.
#    s is guaranteed to be a valid input.
#    All the integers in s are in the range [1, 300].

class Solution:
    def decodeString(self, s: str) -> str:
        """Stack-based approach"""
        stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current state to stack
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop and repeat
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else:
                current_string += char

        return current_string


class SolutionRecursive:
    """Recursive descent approach"""

    def decodeString(self, s: str) -> str:
        self.idx = 0

        def decode():
            result = ""

            while self.idx < len(s) and s[self.idx] != ']':
                if s[self.idx].isdigit():
                    # Parse number
                    num = 0
                    while self.idx < len(s) and s[self.idx].isdigit():
                        num = num * 10 + int(s[self.idx])
                        self.idx += 1

                    self.idx += 1  # Skip '['
                    decoded = decode()
                    self.idx += 1  # Skip ']'

                    result += decoded * num
                else:
                    result += s[self.idx]
                    self.idx += 1

            return result

        return decode()


class SolutionTwoStacks:
    """Using two separate stacks"""

    def decodeString(self, s: str) -> str:
        string_stack = [""]
        num_stack = []
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                string_stack.append("")
                current_num = 0
            elif char == ']':
                num = num_stack.pop()
                inner = string_stack.pop()
                string_stack[-1] += inner * num
            else:
                string_stack[-1] += char

        return string_stack[0]
