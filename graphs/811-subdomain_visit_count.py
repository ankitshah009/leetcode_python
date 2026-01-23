#811. Subdomain Visit Count
#Medium
#
#A website domain "discuss.leetcode.com" consists of various subdomains. At the
#top level, we have "com", at the next level, we have "leetcode.com" and at the
#lowest level, "discuss.leetcode.com". When we visit a domain like
#"discuss.leetcode.com", we will also visit the parent domains "leetcode.com"
#and "com" implicitly.
#
#A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3"
#or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is
#the domain itself.
#
#Given an array of count-paired domains cpdomains, return an array of the
#count-paired domains of each subdomain in the input. You may return the answer
#in any order.
#
#Example 1:
#Input: cpdomains = ["9001 discuss.leetcode.com"]
#Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
#
#Example 2:
#Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
#Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
#
#Constraints:
#    1 <= cpdomains.length <= 100
#    1 <= cpdomains[i].length <= 100
#    cpdomains[i] follows either "repi d1i.d2i.d3i" or "repi d1i.d2i" format.
#    repi is an integer in the range [1, 10^4].
#    d1i, d2i, and d3i consist of lowercase English letters.

from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        """
        Parse each domain and count all subdomains.
        """
        counts = Counter()

        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)

            # Add all subdomains
            parts = domain.split('.')
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                counts[subdomain] += count

        return [f"{count} {domain}" for domain, count in counts.items()]


class SolutionExplicit:
    """More explicit parsing"""

    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        from collections import defaultdict

        visit_count = defaultdict(int)

        for cpdomain in cpdomains:
            space_idx = cpdomain.index(' ')
            count = int(cpdomain[:space_idx])
            domain = cpdomain[space_idx + 1:]

            # Generate all subdomains
            while domain:
                visit_count[domain] += count
                dot_idx = domain.find('.')
                if dot_idx == -1:
                    break
                domain = domain[dot_idx + 1:]

        return [f"{cnt} {dom}" for dom, cnt in visit_count.items()]
