#853. Car Fleet
#Medium
#
#There are n cars going to the same destination along a one-lane road. The
#destination is target miles away.
#
#You are given two integer arrays position and speed, both of length n, where
#position[i] is the position of the ith car and speed[i] is the speed of the
#ith car (in miles per hour).
#
#A car can never pass another car ahead of it, but it can catch up to it and
#drive bumper to bumper at the same speed. The faster car will slow down to
#match the slower car's speed. The distance between these two cars is ignored.
#
#A car fleet is some non-empty set of cars driving at the same position and
#same speed. Note that a single car is also a car fleet.
#
#If a car catches up to a car fleet right at the destination point, it will
#still be considered as one car fleet.
#
#Return the number of car fleets that will arrive at the destination.
#
#Example 1:
#Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
#Output: 3
#
#Example 2:
#Input: target = 10, position = [3], speed = [3]
#Output: 1
#
#Example 3:
#Input: target = 100, position = [0,2,4], speed = [4,2,1]
#Output: 1
#
#Constraints:
#    n == position.length == speed.length
#    1 <= n <= 10^5
#    0 < target <= 10^6
#    0 <= position[i] < target
#    All the values of position are unique.
#    0 < speed[i] <= 10^6

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """
        Sort by position descending.
        Car forms new fleet if its time to target > previous fleet's time.
        """
        # Pair and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        prev_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > prev_time:
                fleets += 1
                prev_time = time

        return fleets


class SolutionStack:
    """Stack-based approach"""

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # Times to reach target

        for pos, spd in cars:
            time = (target - pos) / spd

            # If this car is slower (takes longer), it's a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


class SolutionCounting:
    """Count fleets directly"""

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Calculate time to reach target for each car
        times = [(target - p) / s for p, s in zip(position, speed)]

        # Sort by position descending
        sorted_times = [t for _, t in sorted(zip(position, times), reverse=True)]

        fleets = 0
        max_time = 0

        for time in sorted_times:
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets
