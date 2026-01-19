#294. Flip Game II
#Medium
#
#You are playing a Flip Game with your friend.
#
#You are given a string currentState that contains only '+' and '-'. You and your
#friend take turns to flip two consecutive "++" into "--". The game ends when a
#person can no longer make a move, and therefore the other person will be the winner.
#
#Return true if the starting player can guarantee a win, and false otherwise.
#
#Example 1:
#Input: currentState = "++++"
#Output: true
#Explanation: The starting player can guarantee a win by flipping the middle "++"
#to become "+--+".
#
#Example 2:
#Input: currentState = "+"
#Output: false
#
#Constraints:
#    1 <= currentState.length <= 60
#    currentState[i] is either '+' or '-'.
#
#Follow up: Derive your algorithm's runtime complexity.

class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}

        def can_win(state):
            if state in memo:
                return memo[state]

            # Try all possible moves
            for i in range(len(state) - 1):
                if state[i] == '+' and state[i + 1] == '+':
                    # Make move
                    next_state = state[:i] + '--' + state[i + 2:]

                    # If opponent cannot win from next_state, we win
                    if not can_win(next_state):
                        memo[state] = True
                        return True

            # No winning move found
            memo[state] = False
            return False

        return can_win(currentState)

    # Using game theory (Sprague-Grundy theorem)
    def canWinSG(self, currentState: str) -> bool:
        # Find all groups of consecutive '+'
        def get_grundy(length, memo={}):
            if length in memo:
                return memo[length]

            if length < 2:
                return 0

            reachable = set()
            for i in range(length - 1):
                # Split into two groups of length i and length-i-2
                left = i
                right = length - i - 2
                reachable.add(get_grundy(left) ^ get_grundy(right))

            # Find minimum excludant (mex)
            mex = 0
            while mex in reachable:
                mex += 1

            memo[length] = mex
            return mex

        # Find lengths of all consecutive '+' groups
        xor_sum = 0
        count = 0

        for char in currentState + '-':  # Add '-' to handle last group
            if char == '+':
                count += 1
            else:
                if count > 0:
                    xor_sum ^= get_grundy(count)
                count = 0

        return xor_sum != 0
