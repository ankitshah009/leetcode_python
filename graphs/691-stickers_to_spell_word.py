#691. Stickers to Spell Word
#Hard
#
#We are given n different types of stickers. Each sticker has a lowercase
#English word on it.
#
#You would like to spell out the given string target by cutting individual
#letters from your collection of stickers and rearranging them. You can use
#each sticker more than once if you want, and you have infinite quantities
#of each sticker.
#
#Return the minimum number of stickers that you need to spell out target.
#If the task is impossible, return -1.
#
#Example 1:
#Input: stickers = ["with","example","science"], target = "thehat"
#Output: 3
#Explanation: We can use 2 "with" stickers, and 1 "example" sticker.
#
#Example 2:
#Input: stickers = ["notice","possible"], target = "basicbasic"
#Output: -1
#Explanation: We cannot form "basicbasic" from cutting letters.
#
#Constraints:
#    n == stickers.length
#    1 <= n <= 50
#    1 <= stickers[i].length <= 10
#    1 <= target.length <= 15
#    stickers[i] and target consist of lowercase English letters.

from collections import Counter
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        """
        DP with bitmask: state represents which chars of target are covered.
        """
        n = len(target)
        sticker_counts = [Counter(s) for s in stickers]

        @lru_cache(maxsize=None)
        def dp(remaining):
            if not remaining:
                return 0

            remaining_count = Counter(remaining)
            min_stickers = float('inf')

            for sticker in sticker_counts:
                # Only try stickers that have the first char of remaining
                if sticker[remaining[0]] == 0:
                    continue

                # Apply this sticker
                new_remaining = []
                temp_count = remaining_count.copy()

                for c, cnt in sticker.items():
                    temp_count[c] -= cnt

                for c in remaining:
                    if temp_count[c] > 0:
                        new_remaining.append(c)
                        temp_count[c] -= 1

                result = dp(''.join(new_remaining))
                if result != -1:
                    min_stickers = min(min_stickers, result + 1)

            return min_stickers if min_stickers != float('inf') else -1

        return dp(target)


class SolutionBFS:
    """BFS approach with state as remaining target"""

    def minStickers(self, stickers: list[str], target: str) -> int:
        from collections import deque

        sticker_counts = [Counter(s) for s in stickers]

        # Check if target is possible
        all_chars = Counter()
        for sc in sticker_counts:
            all_chars |= sc
        for c in target:
            if c not in all_chars:
                return -1

        queue = deque([(target, 0)])
        visited = {target}

        while queue:
            remaining, steps = queue.popleft()

            if not remaining:
                return steps

            # Try each sticker
            for sticker in sticker_counts:
                if sticker[remaining[0]] == 0:
                    continue

                # Apply sticker
                new_remaining = list(remaining)
                temp = sticker.copy()

                for i in range(len(new_remaining) - 1, -1, -1):
                    if temp[new_remaining[i]] > 0:
                        temp[new_remaining[i]] -= 1
                        new_remaining.pop(i)

                new_state = ''.join(sorted(new_remaining))

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

        return -1
