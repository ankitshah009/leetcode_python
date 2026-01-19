#93. Restore IP Addresses
#Medium
#
#A valid IP address consists of exactly four integers separated by single dots. Each integer
#is between 0 and 255 (inclusive) and cannot have leading zeros.
#
#Given a string s containing only digits, return all possible valid IP addresses that can be
#formed by inserting dots into s.
#
#Example 1:
#Input: s = "25525511135"
#Output: ["255.255.11.135","255.255.111.35"]
#
#Example 2:
#Input: s = "0000"
#Output: ["0.0.0.0"]
#
#Example 3:
#Input: s = "101023"
#Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#Constraints:
#    1 <= s.length <= 20
#    s consists of digits only.

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def is_valid(segment):
            if len(segment) > 3:
                return False
            if len(segment) > 1 and segment[0] == '0':
                return False
            return int(segment) <= 255

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append('.'.join(parts))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if is_valid(segment):
                    backtrack(end, parts + [segment])

        backtrack(0, [])
        return result
