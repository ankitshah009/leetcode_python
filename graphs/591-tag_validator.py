#591. Tag Validator
#Hard
#
#Given a string representing a code snippet, implement a tag validator to parse
#the code and return whether it is valid.
#
#A code snippet is valid if all the following rules hold:
#1. The code must be wrapped in a valid closed tag.
#2. A closed tag has the form <TAG_NAME>TAG_CONTENT</TAG_NAME>.
#3. TAG_NAME is uppercase English letters only, with length in range [1,9].
#4. TAG_CONTENT may contain other valid closed tags, cdata and any characters
#   except unmatched <, unmatched start and end tag.
#5. CDATA has the form <![CDATA[CDATA_CONTENT]]>.
#
#Constraints:
#    1 <= code.length <= 500
#    code consists of English letters, digits, and special characters.

class Solution:
    def isValid(self, code: str) -> bool:
        """Stack-based tag validation"""
        stack = []
        i = 0
        n = len(code)

        while i < n:
            if i > 0 and not stack:
                return False

            if code[i:i+9] == '<![CDATA[':
                # Find CDATA end
                j = code.find(']]>', i + 9)
                if j < 0:
                    return False
                i = j + 3

            elif code[i:i+2] == '</':
                # End tag
                j = code.find('>', i + 2)
                if j < 0:
                    return False

                tag_name = code[i+2:j]
                if not self.is_valid_tag_name(tag_name):
                    return False
                if not stack or stack[-1] != tag_name:
                    return False
                stack.pop()
                i = j + 1

            elif code[i] == '<':
                # Start tag
                j = code.find('>', i + 1)
                if j < 0:
                    return False

                tag_name = code[i+1:j]
                if not self.is_valid_tag_name(tag_name):
                    return False
                stack.append(tag_name)
                i = j + 1

            else:
                i += 1

        return len(stack) == 0

    def is_valid_tag_name(self, name: str) -> bool:
        return 1 <= len(name) <= 9 and name.isupper() and name.isalpha()


class SolutionRegex:
    """Using regex for validation"""

    def isValid(self, code: str) -> bool:
        import re

        # Replace CDATA sections
        while True:
            new_code = re.sub(r'<!\[CDATA\[.*?\]\]>', '#', code, flags=re.DOTALL)
            if new_code == code:
                break
            code = new_code

        # Match and remove tags from inside out
        while True:
            new_code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', '', code)
            if new_code == code:
                break
            code = new_code

        return code == ''
