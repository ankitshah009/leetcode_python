#929. Unique Email Addresses
#Easy
#
#Every valid email consists of a local name and a domain name, separated by '@'.
#
#Besides lowercase letters, the email may contain one or more '.' or '+'.
#
#For example, in "alice@leetcode.com", "alice" is the local name, and
#"leetcode.com" is the domain name.
#
#If you add periods '.' between some characters in the local name, mail sent
#there will be forwarded to the same address without dots. Note that this rule
#does not apply to domain names.
#
#If you add a plus '+' in the local name, everything after the first plus sign
#will be ignored. This allows certain emails to be filtered.
#
#Return the number of different addresses that actually receive mails.
#
#Example 1:
#Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
#                 "testemail+david@lee.tcode.com"]
#Output: 2
#
#Constraints:
#    1 <= emails.length <= 100
#    1 <= emails[i].length <= 100
#    emails[i] consist of lowercase English letters, '+', '.' and '@'.
#    Each emails[i] contains exactly one '@' character.
#    All local and domain names are non-empty.
#    Local names do not start with a '+' character.
#    Domain names end with the ".com" suffix.

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Normalize each email and count unique ones.
        """
        unique = set()

        for email in emails:
            local, domain = email.split('@')

            # Remove everything after '+'
            local = local.split('+')[0]

            # Remove dots
            local = local.replace('.', '')

            unique.add(local + '@' + domain)

        return len(unique)


class SolutionExplicit:
    """More explicit parsing"""

    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()

        for email in emails:
            at_idx = email.index('@')
            local = email[:at_idx]
            domain = email[at_idx + 1:]

            # Process local name
            normalized = []
            for c in local:
                if c == '+':
                    break
                if c != '.':
                    normalized.append(c)

            unique.add(''.join(normalized) + '@' + domain)

        return len(unique)


class SolutionRegex:
    """Using regex"""

    def numUniqueEmails(self, emails: list[str]) -> int:
        import re

        unique = set()

        for email in emails:
            local, domain = email.split('@')
            local = re.sub(r'\+.*', '', local)  # Remove + and after
            local = local.replace('.', '')  # Remove dots
            unique.add(f"{local}@{domain}")

        return len(unique)
