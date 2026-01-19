#293. Flip Game
#Easy
#
#You are playing a Flip Game with your friend.
#
#You are given a string currentState that contains only '+' and '-'. You and
#your friend take turns to flip two consecutive "++" into "--". The game ends
#when a person can no longer make a move, and therefore the other person will
#be the winner.
#
#Return all possible states of the string currentState after one valid move.
#You may return the answer in any order. If there is no valid move, return an
#empty list [].
#
#Example 1:
#Input: currentState = "++++"
#Output: ["--++","+--+","++--"]
#
#Example 2:
#Input: currentState = "+"
#Output: []
#
#Constraints:
#    1 <= currentState.length <= 500
#    currentState[i] is either '+' or '-'.

from typing import List

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []

        for i in range(len(currentState) - 1):
            if currentState[i:i+2] == '++':
                # Flip these two characters
                new_state = currentState[:i] + '--' + currentState[i+2:]
                result.append(new_state)

        return result


class SolutionList:
    """Using list for string manipulation"""

    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []
        chars = list(currentState)

        for i in range(len(chars) - 1):
            if chars[i] == '+' and chars[i+1] == '+':
                chars[i] = chars[i+1] = '-'
                result.append(''.join(chars))
                chars[i] = chars[i+1] = '+'  # Restore

        return result


class SolutionGenerator:
    """Using generator"""

    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        return [
            currentState[:i] + '--' + currentState[i+2:]
            for i in range(len(currentState) - 1)
            if currentState[i:i+2] == '++'
        ]
