#789. Escape The Ghosts
#Medium
#
#You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start
#at the point [0, 0], and you are given a destination point target = [xtarget,
#ytarget] that you are trying to get to. There are several ghosts on the map
#with their starting positions given as a 2D array ghosts, where ghosts[i] =
#[xi, yi] represents the starting position of the ith ghost.
#
#Each turn, you and all the ghosts may independently choose to either move 1
#unit in any of the four cardinal directions: north, east, south, or west, or
#stay still. All actions happen simultaneously.
#
#You escape if and only if you can reach the target before any ghost reaches
#you. If you reach any square (including the target) at the same time as a
#ghost, it does not count as an escape.
#
#Return true if it is possible to escape, or false otherwise.
#
#Example 1:
#Input: ghosts = [[1,0],[0,3]], target = [0,1]
#Output: true
#
#Example 2:
#Input: ghosts = [[1,0]], target = [2,0]
#Output: false
#
#Example 3:
#Input: ghosts = [[2,0]], target = [1,0]
#Output: false
#
#Constraints:
#    1 <= ghosts.length <= 100
#    ghosts[i].length == 2
#    -10^4 <= xi, yi <= 10^4
#    There can be multiple ghosts in the same location.
#    target.length == 2
#    -10^4 <= xtarget, ytarget <= 10^4

class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        """
        Key insight: if any ghost can reach target in <= my distance,
        they can intercept me. Ghosts should go straight to target.
        """
        my_dist = abs(target[0]) + abs(target[1])

        for gx, gy in ghosts:
            ghost_dist = abs(gx - target[0]) + abs(gy - target[1])
            if ghost_dist <= my_dist:
                return False

        return True


class SolutionCompact:
    """Compact one-liner"""

    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        my_dist = abs(target[0]) + abs(target[1])
        return all(
            abs(g[0] - target[0]) + abs(g[1] - target[1]) > my_dist
            for g in ghosts
        )
