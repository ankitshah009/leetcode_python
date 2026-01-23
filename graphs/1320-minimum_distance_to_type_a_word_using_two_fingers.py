#1320. Minimum Distance to Type a Word Using Two Fingers
#Hard
#
#You have a keyboard layout as shown in the picture. Each English uppercase
#letter is located at some coordinate.
#
#A B C D E F
#G H I J K L
#M N O P Q R
#S T U V W X
#Y Z
#
#Given a string word, return the minimum total distance to type such string
#using only two fingers.
#
#The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.
#
#Note that the initial positions of your two fingers are considered free so
#your first finger could be at any letter and the second finger could be at
#any letter.
#
#Example 1:
#Input: word = "CAKE"
#Output: 3
#Explanation: Using two fingers, one optimal way to type "CAKE" is:
#Finger 1 on letter 'C' -> cost = 0
#Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2
#Finger 2 on letter 'K' -> cost = 0
#Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1
#Total distance = 3
#
#Example 2:
#Input: word = "HAPPY"
#Output: 6
#Explanation: Using two fingers, one optimal way to type "HAPPY" is:
#Finger 1 on letter 'H' -> cost = 0
#Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
#Finger 2 on letter 'P' -> cost = 0
#Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
#Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
#Total distance = 6
#
#Constraints:
#    2 <= word.length <= 300
#    word consists of uppercase English letters.

from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        DP with state (index, finger1_pos, finger2_pos).
        Optimize by only tracking one finger position since the other
        must be at previous letter.
        """
        def get_pos(c):
            idx = ord(c) - ord('A')
            return (idx // 6, idx % 6)

        def dist(c1, c2):
            if c1 is None:
                return 0
            p1, p2 = get_pos(c1), get_pos(c2)
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(word)

        @lru_cache(maxsize=None)
        def dp(idx, other_finger):
            """
            At position idx, one finger is at word[idx-1], other at other_finger.
            Return min cost to finish typing.
            """
            if idx == n:
                return 0

            curr = word[idx]
            prev = word[idx - 1] if idx > 0 else None

            # Option 1: Use the finger that's at prev position
            cost1 = dist(prev, curr) + dp(idx + 1, other_finger)

            # Option 2: Use the other finger
            cost2 = dist(other_finger, curr) + dp(idx + 1, prev)

            return min(cost1, cost2)

        return dp(0, None)


class SolutionBottomUp:
    def minimumDistance(self, word: str) -> int:
        """Bottom-up DP"""
        def get_pos(c):
            idx = ord(c) - ord('A')
            return (idx // 6, idx % 6)

        def dist(i, j):
            if i == 26:  # Initial position (free)
                return 0
            p1 = (i // 6, i % 6)
            p2 = (j // 6, j % 6)
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(word)
        letters = [ord(c) - ord('A') for c in word]

        # dp[i][j] = min distance when finger1 is at letter i, finger2 at letter j
        # Use 26 to represent "not placed yet"
        INF = float('inf')

        # dp[other] = min cost when one finger is at prev letter, other at position 'other'
        dp = {26: 0}  # other finger not placed yet

        for i in range(n):
            new_dp = {}
            curr = letters[i]

            for other, cost in dp.items():
                # Determine where first finger is
                prev = letters[i - 1] if i > 0 else 26

                # Move first finger (at prev) to curr
                key = other
                d = dist(prev, curr)
                if key not in new_dp or new_dp[key] > cost + d:
                    new_dp[key] = cost + d

                # Move other finger to curr
                key = prev
                d = dist(other, curr)
                if key not in new_dp or new_dp[key] > cost + d:
                    new_dp[key] = cost + d

            dp = new_dp

        return min(dp.values())


class Solution3D:
    def minimumDistance(self, word: str) -> int:
        """Full 3D DP for clarity"""
        def dist(a, b):
            if a == -1:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        n = len(word)
        letters = [ord(c) - ord('A') for c in word]

        # dp[i][f1][f2] = min cost to type word[0:i] with fingers at f1, f2
        INF = float('inf')
        dp = [[INF] * 27 for _ in range(27)]
        dp[26][26] = 0  # Both fingers at "nowhere" (-1 represented as 26)

        for char in letters:
            new_dp = [[INF] * 27 for _ in range(27)]

            for f1 in range(27):
                for f2 in range(27):
                    if dp[f1][f2] == INF:
                        continue

                    # Move finger 1 to current char
                    cost = dp[f1][f2] + dist(f1 if f1 < 26 else -1, char)
                    new_dp[char][f2] = min(new_dp[char][f2], cost)

                    # Move finger 2 to current char
                    cost = dp[f1][f2] + dist(f2 if f2 < 26 else -1, char)
                    new_dp[f1][char] = min(new_dp[f1][char], cost)

            dp = new_dp

        return min(dp[f1][f2] for f1 in range(27) for f2 in range(27))
