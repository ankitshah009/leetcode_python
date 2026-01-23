#1653. Minimum Deletions to Make String Balanced
#Medium
#
#You are given a string s consisting only of characters 'a' and 'b'.
#
#You can delete any number of characters in s to make s balanced. s is balanced
#if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j] = 'a'.
#
#Return the minimum number of deletions needed to make s balanced.
#
#Example 1:
#Input: s = "aababbab"
#Output: 2
#Explanation: Delete the characters at indices 2 and 6 ("aababbab" -> "aaabbb").
#
#Example 2:
#Input: s = "bbaaaaabb"
#Output: 2
#Explanation: Delete first two characters or last two characters.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is 'a' or 'b'.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        DP approach: track count of 'b's seen and deletions needed.
        At each 'a', either delete it or delete all 'b's before it.
        """
        b_count = 0
        deletions = 0

        for c in s:
            if c == 'b':
                b_count += 1
            else:  # c == 'a'
                # Either delete this 'a' or delete all 'b's before
                deletions = min(deletions + 1, b_count)

        return deletions


class SolutionDP:
    def minimumDeletions(self, s: str) -> int:
        """
        DP with explicit state tracking.
        dp[i] = min deletions to make s[0:i] balanced
        """
        n = len(s)
        dp = [0] * (n + 1)
        b_count = 0

        for i in range(n):
            if s[i] == 'b':
                dp[i + 1] = dp[i]
                b_count += 1
            else:
                # Delete this 'a' or keep it (delete all 'b's before)
                dp[i + 1] = min(dp[i] + 1, b_count)

        return dp[n]


class SolutionPrefixSuffix:
    def minimumDeletions(self, s: str) -> int:
        """
        Find optimal split point.
        Delete all 'b's before point + all 'a's after point.
        """
        n = len(s)

        # suffix_a[i] = count of 'a's from index i to end
        suffix_a = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_a[i] = suffix_a[i + 1] + (1 if s[i] == 'a' else 0)

        # Try each split point
        min_deletions = suffix_a[0]  # Delete all 'a's
        prefix_b = 0

        for i in range(n):
            if s[i] == 'b':
                prefix_b += 1
            min_deletions = min(min_deletions, prefix_b + suffix_a[i + 1])

        return min_deletions


class SolutionStack:
    def minimumDeletions(self, s: str) -> int:
        """
        Stack-based approach: remove 'ba' pairs.
        """
        deletions = 0
        b_stack = 0

        for c in s:
            if c == 'b':
                b_stack += 1
            elif b_stack > 0:
                # Found 'ba' pair, delete one
                b_stack -= 1
                deletions += 1

        return deletions


class SolutionCounting:
    def minimumDeletions(self, s: str) -> int:
        """
        Count-based approach with running minimum.
        """
        total_a = s.count('a')
        b_count = 0
        a_count = 0
        min_del = total_a  # Delete all 'a's

        for c in s:
            if c == 'a':
                a_count += 1
            else:
                b_count += 1

            # At this point:
            # - 'a's after current position = total_a - a_count
            # - 'b's before or at current position = b_count
            remaining_a = total_a - a_count
            min_del = min(min_del, b_count + remaining_a)

        return min_del
