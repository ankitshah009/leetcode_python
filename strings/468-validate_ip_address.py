#468. Validate IP Address
#Medium
#
#Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid
#IPv6 address or "Neither" if IP is not a correct IP of any type.
#
#A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot
#contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses
#while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.
#
#A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
#    1 <= xi.length <= 4
#    xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f')
#    and upper-case English letters ('A' to 'F').
#    Leading zeros are allowed in xi.
#
#For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334"
#are valid IPv6 addresses.
#
#Example 1:
#Input: queryIP = "172.16.254.1"
#Output: "IPv4"
#
#Example 2:
#Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
#Output: "IPv6"
#
#Example 3:
#Input: queryIP = "256.256.256.256"
#Output: "Neither"
#
#Constraints:
#    queryIP consists only of English letters, digits and the characters '.' and ':'.

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False

            for part in parts:
                if not part or len(part) > 3:
                    return False
                if not part.isdigit():
                    return False
                if len(part) > 1 and part[0] == '0':
                    return False
                if int(part) > 255:
                    return False

            return True

        def is_valid_ipv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False

            hex_chars = set('0123456789abcdefABCDEF')

            for part in parts:
                if not part or len(part) > 4:
                    return False
                if not all(c in hex_chars for c in part):
                    return False

            return True

        if '.' in queryIP:
            return "IPv4" if is_valid_ipv4(queryIP) else "Neither"
        elif ':' in queryIP:
            return "IPv6" if is_valid_ipv6(queryIP) else "Neither"

        return "Neither"
