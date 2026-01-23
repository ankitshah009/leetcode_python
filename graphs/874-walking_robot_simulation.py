#874. Walking Robot Simulation
#Medium
#
#A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot
#can receive a sequence of these three possible types of commands:
#- -2: Turn left 90 degrees.
#- -1: Turn right 90 degrees.
#- 1 <= k <= 9: Move forward k units, one unit at a time.
#
#Some of the grid squares are obstacles. The ith obstacle is at grid point
#obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will instead
#stay in its current location and move on to the next command.
#
#Return the maximum Euclidean distance squared that the robot ever gets from
#the origin (i.e., max of x^2 + y^2).
#
#Example 1:
#Input: commands = [4,-1,3], obstacles = []
#Output: 25
#Explanation: Robot goes to (0, 4) then (3, 4). Max distance squared = 25.
#
#Example 2:
#Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
#Output: 65
#Explanation: Robot ends at (1, 8). Max = 1 + 64 = 65.
#
#Constraints:
#    1 <= commands.length <= 10^4
#    commands[i] is either -2, -1, or an integer in the range [1, 9].
#    0 <= obstacles.length <= 10^4
#    -3 * 10^4 <= xi, yi <= 3 * 10^4
#    The answer is guaranteed to be less than 2^31.

class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        """
        Simulate robot movement with obstacle checking.
        """
        # Directions: North, East, South, West
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        obstacle_set = set(map(tuple, obstacles))

        x, y = 0, 0
        direction = 0  # 0=North, 1=East, 2=South, 3=West
        max_dist = 0

        for cmd in commands:
            if cmd == -2:  # Turn left
                direction = (direction - 1) % 4
            elif cmd == -1:  # Turn right
                direction = (direction + 1) % 4
            else:  # Move forward
                for _ in range(cmd):
                    nx, ny = x + dx[direction], y + dy[direction]
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        max_dist = max(max_dist, x * x + y * y)

        return max_dist


class SolutionDict:
    """Using dictionary for directions"""

    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
        obstacle_set = set(map(tuple, obstacles))

        x, y, d = 0, 0, 0
        max_dist = 0

        for cmd in commands:
            if cmd == -2:
                d = (d - 1) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                dx, dy = directions[d]
                for _ in range(cmd):
                    if (x + dx, y + dy) not in obstacle_set:
                        x, y = x + dx, y + dy
                max_dist = max(max_dist, x * x + y * y)

        return max_dist


class SolutionComplex:
    """Using complex numbers for direction"""

    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacle_set = {complex(x, y) for x, y in obstacles}

        pos = 0j  # Current position
        direction = 1j  # Facing north (positive imaginary)
        max_dist = 0

        for cmd in commands:
            if cmd == -2:  # Turn left
                direction *= 1j
            elif cmd == -1:  # Turn right
                direction *= -1j
            else:
                for _ in range(cmd):
                    if pos + direction not in obstacle_set:
                        pos += direction
                max_dist = max(max_dist, int(pos.real**2 + pos.imag**2))

        return max_dist
