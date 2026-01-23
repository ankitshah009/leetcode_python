#943. Find the Shortest Superstring
#Hard
#
#Given an array of strings words, return the shortest string that contains each
#string in words as a substring. If there are multiple valid strings of the
#smallest length, return any of them.
#
#You may assume that no string in words is a substring of another string in words.
#
#Example 1:
#Input: words = ["alex","loves","leetcode"]
#Output: "alexlovesleetcode"
#Explanation: All permutations would also be accepted.
#
#Example 2:
#Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
#Output: "gctaagttcatgcatc"
#
#Constraints:
#    1 <= words.length <= 12
#    1 <= words[i].length <= 20
#    words[i] consists of lowercase English letters.
#    All the strings of words are unique.

class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:
        """
        Traveling Salesman Problem with DP bitmask.
        """
        n = len(words)

        # overlap[i][j] = length of overlap when appending words[j] after words[i]
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    for k in range(min(len(words[i]), len(words[j])), 0, -1):
                        if words[i][-k:] == words[j][:k]:
                            overlap[i][j] = k
                            break

        # dp[mask][i] = (max overlap, parent) ending at word i with mask visited
        dp = [[(-1, -1)] * n for _ in range(1 << n)]

        # Initialize single words
        for i in range(n):
            dp[1 << i][i] = (0, -1)

        # Fill DP
        for mask in range(1, 1 << n):
            for last in range(n):
                if not (mask & (1 << last)):
                    continue
                if dp[mask][last][0] == -1:
                    continue

                prev_mask = mask ^ (1 << last)
                if prev_mask == 0:
                    continue

                for prev in range(n):
                    if not (prev_mask & (1 << prev)):
                        continue
                    if dp[prev_mask][prev][0] == -1:
                        continue

                    new_overlap = dp[prev_mask][prev][0] + overlap[prev][last]
                    if new_overlap > dp[mask][last][0]:
                        dp[mask][last] = (new_overlap, prev)

        # Find best ending
        full_mask = (1 << n) - 1
        best_last = 0
        best_overlap = dp[full_mask][0][0]

        for i in range(1, n):
            if dp[full_mask][i][0] > best_overlap:
                best_overlap = dp[full_mask][i][0]
                best_last = i

        # Reconstruct path
        path = []
        mask = full_mask
        curr = best_last

        while curr != -1:
            path.append(curr)
            prev = dp[mask][curr][1]
            mask ^= (1 << curr)
            curr = prev

        path.reverse()

        # Build result string
        result = words[path[0]]
        for i in range(1, len(path)):
            prev_word = path[i - 1]
            curr_word = path[i]
            result += words[curr_word][overlap[prev_word][curr_word]:]

        return result


class SolutionMemo:
    """Memoization with reconstruction"""

    def shortestSuperstring(self, words: list[str]) -> str:
        n = len(words)

        # Precompute overlaps
        def get_overlap(a: str, b: str) -> int:
            for k in range(min(len(a), len(b)), 0, -1):
                if a[-k:] == b[:k]:
                    return k
            return 0

        overlap = [[get_overlap(words[i], words[j]) for j in range(n)] for i in range(n)]

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << last):
                return 0

            best = -1
            for prev in range(n):
                if prev == last or not (mask & (1 << prev)):
                    continue
                prev_mask = mask ^ (1 << last)
                val = dp(prev_mask, prev) + overlap[prev][last]
                if val > best:
                    best = val

            return best

        # Find best last word
        full = (1 << n) - 1
        best_last = max(range(n), key=lambda i: dp(full, i))

        # Reconstruct
        path = []
        mask = full
        last = best_last

        while mask:
            path.append(last)
            if mask == (1 << last):
                break

            prev_mask = mask ^ (1 << last)
            for prev in range(n):
                if prev_mask & (1 << prev):
                    if dp(prev_mask, prev) + overlap[prev][last] == dp(mask, last):
                        mask = prev_mask
                        last = prev
                        break

        path.reverse()

        result = words[path[0]]
        for i in range(1, len(path)):
            result += words[path[i]][overlap[path[i-1]][path[i]]:]

        return result
