#1044. Longest Duplicate Substring
#Hard
#
#Given a string s, consider all duplicated substrings: (contiguous) substrings
#of s that occur 2 or more times. The occurrences may overlap.
#
#Return any duplicated substring that has the longest possible length.
#If s does not have a duplicated substring, the answer is "".
#
#Example 1:
#Input: s = "banana"
#Output: "ana"
#
#Example 2:
#Input: s = "abcd"
#Output: ""
#
#Constraints:
#    2 <= s.length <= 3 * 10^4
#    s consists of lowercase English letters.

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        Binary search on length + Rabin-Karp rolling hash.
        """
        n = len(s)
        MOD = 2**63 - 1
        BASE = 26

        def search(length):
            """Check if duplicate substring of given length exists"""
            if length == 0:
                return 0

            # Compute hash of first window
            h = 0
            for i in range(length):
                h = (h * BASE + ord(s[i]) - ord('a')) % MOD

            seen = {h: [0]}
            base_power = pow(BASE, length, MOD)

            for i in range(1, n - length + 1):
                # Rolling hash: remove leftmost, add rightmost
                h = (h * BASE - (ord(s[i-1]) - ord('a')) * base_power + ord(s[i+length-1]) - ord('a')) % MOD

                if h in seen:
                    # Check for actual match (hash collision possible)
                    current = s[i:i+length]
                    for prev_idx in seen[h]:
                        if s[prev_idx:prev_idx+length] == current:
                            return i
                    seen[h].append(i)
                else:
                    seen[h] = [i]

            return -1

        # Binary search on length
        left, right = 0, n - 1
        result_idx = 0
        result_len = 0

        while left <= right:
            mid = (left + right) // 2
            idx = search(mid)
            if idx != -1:
                result_idx = idx
                result_len = mid
                left = mid + 1
            else:
                right = mid - 1

        return s[result_idx:result_idx + result_len]


class SolutionSuffixArray:
    def longestDupSubstring(self, s: str) -> str:
        """
        Suffix array approach - O(n log n) construction.
        LCP array to find longest repeated substring.
        """
        n = len(s)

        # Build suffix array using prefix doubling
        sa = list(range(n))
        rank = [ord(c) for c in s]
        tmp = [0] * n
        k = 1

        while k < n:
            def key(i):
                return (rank[i], rank[i + k] if i + k < n else -1)

            sa.sort(key=key)

            tmp[sa[0]] = 0
            for i in range(1, n):
                tmp[sa[i]] = tmp[sa[i-1]]
                if key(sa[i]) != key(sa[i-1]):
                    tmp[sa[i]] += 1

            rank = tmp[:]
            if rank[sa[-1]] == n - 1:
                break
            k *= 2

        # Build LCP array
        lcp = [0] * n
        k = 0
        for i in range(n):
            if rank[i] == 0:
                continue
            j = sa[rank[i] - 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            lcp[rank[i]] = k
            k = max(k - 1, 0)

        # Find maximum LCP
        max_lcp = max(lcp) if lcp else 0
        if max_lcp == 0:
            return ""

        idx = lcp.index(max_lcp)
        return s[sa[idx]:sa[idx] + max_lcp]
