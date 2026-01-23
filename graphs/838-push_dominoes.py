#838. Push Dominoes
#Medium
#
#There are n dominoes in a line, and we place each domino vertically upright.
#In the beginning, we simultaneously push some of the dominoes either to the
#left or to the right.
#
#After each second, each domino that is falling to the left pushes the adjacent
#domino on the left. Similarly, the dominoes falling to the right push their
#adjacent dominoes standing on the right.
#
#When a vertical domino has dominoes falling on it from both sides, it stays
#still due to the balance of the forces.
#
#For the purposes of this question, we will consider that a falling domino
#expends no additional force to a falling or already fallen domino.
#
#You are given a string dominoes representing the initial state where:
#- dominoes[i] = 'L', if the ith domino has been pushed to the left,
#- dominoes[i] = 'R', if the ith domino has been pushed to the right, and
#- dominoes[i] = '.', if the ith domino has not been pushed.
#
#Return a string representing the final state.
#
#Example 1:
#Input: dominoes = "RR.L"
#Output: "RR.L"
#
#Example 2:
#Input: dominoes = ".L.R...LR..L.."
#Output: "LL.RR.LLRRLL.."
#
#Constraints:
#    n == dominoes.length
#    1 <= n <= 10^5
#    dominoes[i] is either 'L', 'R', or '.'.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        For each segment between forces, determine final state.
        Process segments: L...L, R...R, L...R, R...L
        """
        n = len(dominoes)
        forces = [0] * n

        # Right force (decreasing from R)
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Left force (decreasing from L)
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)


class SolutionTwoPointer:
    """Process segments between L and R"""

    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'  # Sentinels
        result = []
        i = 0

        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue

            middle = j - i - 1

            if i > 0:
                result.append(dominoes[i])

            if dominoes[i] == dominoes[j]:
                result.append(dominoes[i] * middle)
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                result.append('.' * middle)
            else:  # R...L
                result.append('R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2))

            i = j

        return ''.join(result)


class SolutionBFS:
    """BFS simulation"""

    def pushDominoes(self, dominoes: str) -> str:
        from collections import deque

        n = len(dominoes)
        result = list(dominoes)
        queue = deque()

        # Initial pushed dominoes
        for i, d in enumerate(dominoes):
            if d != '.':
                queue.append((i, d))

        while queue:
            next_queue = []
            affected = {}

            while queue:
                i, direction = queue.popleft()

                if direction == 'L' and i > 0 and result[i - 1] == '.':
                    if i - 1 in affected:
                        affected[i - 1] = '.'  # Balanced
                    else:
                        affected[i - 1] = 'L'
                elif direction == 'R' and i < n - 1 and result[i + 1] == '.':
                    if i + 1 in affected:
                        affected[i + 1] = '.'  # Balanced
                    else:
                        affected[i + 1] = 'R'

            for idx, d in affected.items():
                result[idx] = d
                if d != '.':
                    next_queue.append((idx, d))

            queue = deque(next_queue)

        return ''.join(result)
