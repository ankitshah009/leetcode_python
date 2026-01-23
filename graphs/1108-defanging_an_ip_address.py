#1108. Defanging an IP Address
#Easy
#
#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
#A defanged IP address replaces every period "." with "[.]".
#
#Example 1:
#Input: address = "1.1.1.1"
#Output: "1[.]1[.]1[.]1"
#
#Example 2:
#Input: address = "255.100.50.0"
#Output: "255[.]100[.]50[.]0"
#
#Constraints:
#    The given address is a valid IPv4 address.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        """Simple replace"""
        return address.replace('.', '[.]')


class SolutionJoin:
    def defangIPaddr(self, address: str) -> str:
        """Split and join"""
        return '[.]'.join(address.split('.'))


class SolutionManual:
    def defangIPaddr(self, address: str) -> str:
        """Manual character-by-character"""
        result = []
        for c in address:
            if c == '.':
                result.append('[.]')
            else:
                result.append(c)
        return ''.join(result)
