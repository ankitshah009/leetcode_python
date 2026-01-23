#948. Bag of Tokens
#Medium
#
#You start with an initial power of power, an initial score of 0, and a bag of
#tokens given as an integer array tokens, where each tokens[i] denotes the value
#of token i.
#
#Your goal is to maximize the total score by playing these tokens. In one move,
#you can play an unplayed token in one of the two ways (but not both for the
#same token):
#- Face-up: If your current power >= tokens[i], you may play it, losing
#  tokens[i] power and gaining 1 score.
#- Face-down: If your current score >= 1, you may play it, gaining tokens[i]
#  power and losing 1 score.
#
#Return the maximum possible score you can achieve.
#
#Example 1:
#Input: tokens = [100], power = 50
#Output: 0
#
#Example 2:
#Input: tokens = [200,100], power = 150
#Output: 1
#
#Example 3:
#Input: tokens = [100,200,300,400], power = 200
#Output: 2
#
#Constraints:
#    0 <= tokens.length <= 1000
#    0 <= tokens[i], power < 10^4

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        """
        Greedy: buy cheapest (face-up), sell most expensive (face-down).
        """
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                # Buy cheapest token
                power -= tokens[left]
                score += 1
                max_score = max(max_score, score)
                left += 1
            elif score > 0:
                # Sell most expensive token
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return max_score


class SolutionDeque:
    """Using deque"""

    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        from collections import deque

        tokens = deque(sorted(tokens))
        score = 0
        max_score = 0

        while tokens:
            if power >= tokens[0]:
                power -= tokens.popleft()
                score += 1
                max_score = max(max_score, score)
            elif score > 0 and len(tokens) > 1:
                power += tokens.pop()
                score -= 1
            else:
                break

        return max_score


class SolutionExplicit:
    """More explicit greedy"""

    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        if not tokens:
            return 0

        tokens.sort()
        n = len(tokens)

        if power < tokens[0]:
            return 0

        left, right = 0, n - 1
        score = 0
        max_score = 0

        while left <= right:
            # Greedily buy as many cheap tokens as possible
            while left <= right and power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1

            max_score = max(max_score, score)

            # Sell expensive token if possible and beneficial
            if score > 0 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return max_score
