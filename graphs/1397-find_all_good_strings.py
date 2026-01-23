#1397. Find All Good Strings
#Hard
#
#Given the strings s1 and s2 of size n and the string evil, return the number
#of good strings.
#
#A good string has size n, it is alphabetically greater than or equal to s1,
#it is alphabetically smaller than or equal to s2, and it does not contain the
#string evil as a substring.
#
#Since the answer can be a huge number, return this modulo 10^9 + 7.
#
#Example 1:
#Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
#Output: 51
#Explanation: There are 25 good strings starting with 'a': "aa","ac",...,"az".
#Then there are 25 good strings starting with 'c': "ca","cc",...,"cz" and
#finally there is one good string starting with 'd': "da".
#
#Example 2:
#Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
#Output: 0
#
#Example 3:
#Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
#Output: 2
#
#Constraints:
#    s1.length == n
#    s2.length == n
#    s1 <= s2
#    1 <= n <= 500
#    1 <= evil.length <= 50
#    All strings consist of lowercase English letters.

from functools import lru_cache

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        """
        Digit DP with KMP failure function.
        Count strings <= s2 without evil - Count strings < s1 without evil.

        State: (position, matched_evil_prefix, is_tight)
        Use KMP to track how much of evil has been matched.
        """
        MOD = 10**9 + 7

        # Build KMP failure function for evil
        m = len(evil)
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = fail[j - 1]
            if evil[i] == evil[j]:
                j += 1
            fail[i] = j

        def count_good_leq(s: str) -> int:
            """Count good strings lexicographically <= s"""
            @lru_cache(maxsize=None)
            def dp(pos: int, evil_matched: int, is_tight: bool) -> int:
                # If we've matched all of evil, this string contains evil
                if evil_matched == m:
                    return 0

                # If we've placed all characters
                if pos == n:
                    return 1

                limit = ord(s[pos]) if is_tight else ord('z')
                result = 0

                for c in range(ord('a'), limit + 1):
                    char = chr(c)

                    # Update evil_matched using KMP
                    new_matched = evil_matched
                    while new_matched > 0 and evil[new_matched] != char:
                        new_matched = fail[new_matched - 1]
                    if evil[new_matched] == char:
                        new_matched += 1

                    new_tight = is_tight and (c == limit)

                    result = (result + dp(pos + 1, new_matched, new_tight)) % MOD

                return result

            return dp(0, 0, True)

        # Count good strings in range [s1, s2]
        # = count_good_leq(s2) - count_good_leq(s1) + (s1 is good ? 1 : 0)

        count_s2 = count_good_leq(s2)

        # Decrement s1 to get count_good_lt(s1)
        # Or check if s1 itself is good
        def contains_evil(s: str) -> bool:
            j = 0
            for c in s:
                while j > 0 and evil[j] != c:
                    j = fail[j - 1]
                if evil[j] == c:
                    j += 1
                if j == m:
                    return True
            return False

        s1_good = 1 if not contains_evil(s1) else 0

        # Decrement s1 by 1
        s1_list = list(s1)
        i = n - 1
        while i >= 0 and s1_list[i] == 'a':
            s1_list[i] = 'z'
            i -= 1
        if i >= 0:
            s1_list[i] = chr(ord(s1_list[i]) - 1)
            s1_decremented = ''.join(s1_list)
            count_s1_minus_1 = count_good_leq(s1_decremented)
        else:
            # s1 was "aaa...a", no string < s1
            count_s1_minus_1 = 0

        return (count_s2 - count_s1_minus_1 - s1_good + MOD) % MOD


class SolutionSimplified:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        """
        Simplified: count <= s2 - count < s1
        count < s1 = count <= (s1 - 1)
        """
        MOD = 10**9 + 7

        # KMP failure function
        m = len(evil)
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = fail[j - 1]
            if evil[i] == evil[j]:
                j += 1
            fail[i] = j

        def get_next_state(state: int, c: str) -> int:
            while state > 0 and evil[state] != c:
                state = fail[state - 1]
            if evil[state] == c:
                state += 1
            return state

        def count_leq(s: str) -> int:
            @lru_cache(maxsize=None)
            def dp(pos: int, evil_state: int, tight: bool) -> int:
                if evil_state == m:
                    return 0
                if pos == n:
                    return 1

                upper = s[pos] if tight else 'z'
                total = 0

                for c_ord in range(ord('a'), ord(upper) + 1):
                    c = chr(c_ord)
                    new_state = get_next_state(evil_state, c)
                    new_tight = tight and (c == upper)
                    total = (total + dp(pos + 1, new_state, new_tight)) % MOD

                return total

            return dp(0, 0, True)

        # Decrement s1
        def decrement(s: str) -> str:
            s = list(s)
            i = len(s) - 1
            while i >= 0 and s[i] == 'a':
                s[i] = 'z'
                i -= 1
            if i < 0:
                return ""
            s[i] = chr(ord(s[i]) - 1)
            return ''.join(s)

        s1_dec = decrement(s1)

        ans_s2 = count_leq(s2)
        ans_s1 = count_leq(s1_dec) if s1_dec else 0

        return (ans_s2 - ans_s1 + MOD) % MOD
