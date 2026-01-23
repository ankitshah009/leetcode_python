#1496. Path Crossing
#Easy
#
#Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
#moving one unit north, south, east, or west, respectively. You start at the
#origin (0, 0) on a 2D plane and walk on the path specified by path.
#
#Return true if the path crosses itself at any point, that is, if at any time
#you are on a location you have previously visited. Return false otherwise.
#
#Example 1:
#Input: path = "NES"
#Output: false
#Explanation: Notice that the path doesn't cross any point more than once.
#
#Example 2:
#Input: path = "NESWW"
#Output: true
#Explanation: Notice that the path visits the origin twice.
#
#Constraints:
#    1 <= path.length <= 10^4
#    path[i] is either 'N', 'S', 'E', or 'W'.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Track visited positions in a set.
        """
        visited = {(0, 0)}
        x, y = 0, 0

        directions = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        for move in path:
            dx, dy = directions[move]
            x += dx
            y += dy

            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False


class SolutionCompact:
    def isPathCrossing(self, path: str) -> bool:
        """Compact version"""
        visited = {(0, 0)}
        x = y = 0

        for move in path:
            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            else:  # 'W'
                x -= 1

            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False


class SolutionWalrus:
    def isPathCrossing(self, path: str) -> bool:
        """Using walrus operator and generator"""
        visited = {(0, 0)}
        x = y = 0
        moves = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        for move in path:
            dx, dy = moves[move]
            x, y = x + dx, y + dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False


class SolutionPrefix:
    def isPathCrossing(self, path: str) -> bool:
        """Track positions as complex numbers"""
        moves = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}
        pos = 0
        visited = {0}

        for move in path:
            pos += moves[move]
            if pos in visited:
                return True
            visited.add(pos)

        return False
