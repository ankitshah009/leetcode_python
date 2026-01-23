#1041. Robot Bounded In Circle
#Medium
#
#On an infinite plane, a robot initially stands at (0, 0) and faces north.
#Note that:
#    The north direction is the positive direction of the y-axis.
#    The south direction is the negative direction of the y-axis.
#    The east direction is the positive direction of the x-axis.
#    The west direction is the negative direction of the x-axis.
#
#The robot can receive one of three instructions:
#    "G": go straight 1 unit.
#    "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
#    "R": turn 90 degrees to the right (i.e., clockwise direction).
#
#The robot performs the instructions given in order, and repeats them forever.
#
#Return true if and only if there exists a circle in the plane such that the
#robot never leaves the circle.
#
#Example 1:
#Input: instructions = "GGLLGG"
#Output: true
#Explanation: The robot returns to (0, 0) after one cycle.
#
#Example 2:
#Input: instructions = "GG"
#Output: false
#Explanation: The robot moves north indefinitely.
#
#Example 3:
#Input: instructions = "GL"
#Output: true
#Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0).
#
#Constraints:
#    1 <= instructions.length <= 100
#    instructions[i] is 'G', 'L' or 'R'.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        Robot is bounded iff after one cycle:
        1. Returns to origin, OR
        2. Not facing north (will eventually return in 2 or 4 cycles)

        If facing north and not at origin, it will go to infinity.
        """
        # Direction: 0=North, 1=East, 2=South, 3=West
        # dx, dy for each direction
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        direction = 0  # Start facing north

        for instr in instructions:
            if instr == 'G':
                dx, dy = directions[direction]
                x += dx
                y += dy
            elif instr == 'L':
                direction = (direction + 3) % 4  # Turn left
            else:  # R
                direction = (direction + 1) % 4  # Turn right

        # Bounded if at origin OR not facing north
        return (x == 0 and y == 0) or direction != 0


class SolutionSimulation:
    def isRobotBounded(self, instructions: str) -> bool:
        """Simulate 4 cycles - if bounded, must return to origin"""
        x, y = 0, 0
        dx, dy = 0, 1  # Facing north

        for _ in range(4):
            for instr in instructions:
                if instr == 'G':
                    x += dx
                    y += dy
                elif instr == 'L':
                    dx, dy = -dy, dx
                else:
                    dx, dy = dy, -dx

        return x == 0 and y == 0
