#735. Asteroid Collision
#Medium
#
#We are given an array asteroids of integers representing asteroids in a row.
#
#For each asteroid, the absolute value represents its size, and the sign
#represents its direction (positive meaning right, negative meaning left).
#Each asteroid moves at the same speed.
#
#Find out the state of the asteroids after all collisions. If two asteroids
#meet, the smaller one will explode. If both are the same size, both will
#explode. Two asteroids moving in the same direction will never meet.
#
#Example 1:
#Input: asteroids = [5,10,-5]
#Output: [5,10]
#Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
#
#Example 2:
#Input: asteroids = [8,-8]
#Output: []
#Explanation: The 8 and -8 collide exploding each other.
#
#Example 3:
#Input: asteroids = [10,2,-5]
#Output: [10]
#Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
#resulting in 10.
#
#Constraints:
#    2 <= asteroids.length <= 10^4
#    -1000 <= asteroids[i] <= 1000
#    asteroids[i] != 0

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        Stack-based simulation. Collision occurs when stack top is moving
        right (+) and current is moving left (-).
        """
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and stack and asteroid < 0 < stack[-1]:
                # Collision: right-moving vs left-moving
                if stack[-1] < -asteroid:
                    stack.pop()  # Stack top destroyed
                elif stack[-1] == -asteroid:
                    stack.pop()  # Both destroyed
                    alive = False
                else:
                    alive = False  # Current destroyed

            if alive:
                stack.append(asteroid)

        return stack


class SolutionDetailed:
    """More explicit collision handling"""

    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                # Moving right, no collision with existing
                stack.append(a)
            else:
                # Moving left, might collide with right-moving
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()

                if not stack or stack[-1] < 0:
                    # No collision possible
                    stack.append(a)
                elif stack[-1] == -a:
                    # Equal size, both explode
                    stack.pop()
                # else: current asteroid destroyed (stack[-1] > -a)

        return stack


class SolutionRecursive:
    """Recursive approach"""

    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        def process(remaining, result):
            if not remaining:
                return result

            a = remaining[0]
            remaining = remaining[1:]

            if not result or a > 0 or result[-1] < 0:
                result.append(a)
            elif result[-1] == -a:
                result.pop()
            elif result[-1] < -a:
                result.pop()
                return process([a] + list(remaining), result)

            return process(remaining, result)

        return process(asteroids, [])
