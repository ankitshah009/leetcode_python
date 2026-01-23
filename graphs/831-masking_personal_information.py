#831. Masking Personal Information
#Medium
#
#You are given a personal information string s, representing either an email
#address or a phone number. Return the masked personal information using the
#below rules.
#
#Email address:
#- The email address is in the format local@domain.
#- The domain is guaranteed to be "@leetcode.com".
#- Mask all letters except first and last in local part with '*'.
#- All domain letters should be lowercase.
#
#Phone number:
#- The phone number contains 10 to 13 digits.
#- The last 10 digits are local number, rest are country code.
#- Mask format: "***-***-XXXX" where XXXX are last 4 digits.
#- With country code: "+*-***-***-XXXX" or "+**-***-***-XXXX" or "+***-***-***-XXXX"
#
#Example 1:
#Input: s = "LeetCode@LeetCode.com"
#Output: "l*****e@leetcode.com"
#
#Example 2:
#Input: s = "AB@qq.com"
#Output: "a*****b@qq.com"
#
#Example 3:
#Input: s = "1(234)567-890"
#Output: "***-***-7890"
#
#Constraints:
#    s is either a valid email or a phone number.

class Solution:
    def maskPII(self, s: str) -> str:
        """
        Determine if email or phone, then mask accordingly.
        """
        if '@' in s:
            # Email
            return self.mask_email(s)
        else:
            # Phone
            return self.mask_phone(s)

    def mask_email(self, s: str) -> str:
        s = s.lower()
        local, domain = s.split('@')
        return local[0] + '*****' + local[-1] + '@' + domain

    def mask_phone(self, s: str) -> str:
        # Extract digits only
        digits = ''.join(c for c in s if c.isdigit())

        # Last 4 digits visible
        local = '***-***-' + digits[-4:]

        # Country code
        extra = len(digits) - 10
        if extra == 0:
            return local
        else:
            return '+' + '*' * extra + '-' + local


class SolutionRegex:
    """Using regex"""

    def maskPII(self, s: str) -> str:
        import re

        if '@' in s:
            s = s.lower()
            match = re.match(r'(.)(.*)(.)@(.+)', s)
            return match.group(1) + '*****' + match.group(3) + '@' + match.group(4)
        else:
            digits = re.sub(r'\D', '', s)
            country = ['', '+*-', '+**-', '+***-'][len(digits) - 10]
            return country + '***-***-' + digits[-4:]
