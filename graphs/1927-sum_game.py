#1927. Sum Game
#Medium
#
#Alice and Bob take turns playing a game, with Alice starting first.
#
#You are given a string num of even length consisting of digits and '?'
#characters. On each turn, a player will do the following if there is still at
#least one '?' in num:
#1. Choose an index i where num[i] == '?'.
#2. Replace num[i] with any digit between '0' and '9'.
#
#The game ends when there are no more '?' characters in num.
#
#For Bob to win, the sum of the digits in the first half of num must be equal
#to the sum of the digits in the second half. For Alice to win, the sums must
#not be equal.
#
#Assuming Alice and Bob play optimally, return true if Alice will win and false
#if Bob will win.
#
#Example 1:
#Input: num = "5023"
#Output: false
#
#Example 2:
#Input: num = "25??"
#Output: true
#
#Example 3:
#Input: num = "?3295???"
#Output: false
#
#Constraints:
#    2 <= num.length <= 10^5
#    num.length is even.
#    num consists of only digits and '?'.

class Solution:
    def sumGame(self, num: str) -> bool:
        """
        Alice wins if she can make sums unequal, Bob wins if he can equalize.

        Key insight: each '?' pair (one in each half) cancels out.
        After pairing, if sum difference equals 9 * (question marks diff / 2),
        Bob can win by balancing. Otherwise Alice wins.
        """
        n = len(num)
        half = n // 2

        left_sum = 0
        left_questions = 0
        right_sum = 0
        right_questions = 0

        for i in range(half):
            if num[i] == '?':
                left_questions += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_questions += 1
            else:
                right_sum += int(num[i])

        # Sum difference
        sum_diff = left_sum - right_sum
        # Question mark difference
        q_diff = left_questions - right_questions

        # For Bob to win: sum_diff + 9 * (q_diff / 2) == 0
        # Which means: sum_diff == -9 * q_diff / 2
        # Or: 2 * sum_diff + 9 * q_diff == 0

        # If q_diff is odd, Alice wins (she makes final move in one half)
        if q_diff % 2 != 0:
            return True

        # Bob wins if he can balance
        # Each question in left can add [0, 9], each in right can add [0, 9]
        # With optimal play:
        # - If Alice adds x in left, Bob adds (9-x) in right to maintain balance
        # - Or vice versa

        # Condition for Bob to win: 2 * sum_diff + 9 * q_diff == 0
        return 2 * sum_diff + 9 * q_diff != 0


class SolutionExplained:
    def sumGame(self, num: str) -> bool:
        """
        Detailed explanation:

        Let L = sum of digits in left half
        Let R = sum of digits in right half
        Let QL = question marks in left half
        Let QR = question marks in right half

        Total moves = QL + QR (even since total length is even)

        Key insight:
        - If QL + QR is odd, Alice makes last move and wins
        - If one half has more ?, the other must compensate with sum

        For Bob to win with optimal play:
        L + (contribution from QL) = R + (contribution from QR)

        With optimal play, each ? contributes 4.5 on average (pairs of moves
        where Alice plays x and Bob plays 9-x sum to 9).

        Bob wins iff: L - R = 9 * (QR - QL) / 2
        """
        n = len(num)
        half = n // 2

        L = sum(int(c) for c in num[:half] if c != '?')
        R = sum(int(c) for c in num[half:] if c != '?')
        QL = num[:half].count('?')
        QR = num[half:].count('?')

        # Bob wins if: 2(L - R) = 9(QR - QL)
        return 2 * (L - R) != 9 * (QR - QL)
