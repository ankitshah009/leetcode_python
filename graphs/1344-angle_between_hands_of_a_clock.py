#1344. Angle Between Hands of a Clock
#Medium
#
#Given two numbers, hour and minutes, return the smaller angle (in degrees)
#formed between the hour and the minute hand.
#
#Answers within 10^-5 of the actual value will be accepted as correct.
#
#Example 1:
#Input: hour = 12, minutes = 30
#Output: 165
#
#Example 2:
#Input: hour = 3, minutes = 30
#Output: 75
#
#Example 3:
#Input: hour = 3, minutes = 15
#Output: 7.5
#
#Constraints:
#    1 <= hour <= 12
#    0 <= minutes <= 59

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        Calculate angle for each hand from 12 o'clock, then find difference.

        Minute hand: 360 degrees / 60 minutes = 6 degrees per minute
        Hour hand: 360 degrees / 12 hours = 30 degrees per hour
                   Plus movement due to minutes: 0.5 degrees per minute
        """
        # Angle of minute hand from 12 o'clock
        minute_angle = minutes * 6

        # Angle of hour hand from 12 o'clock
        hour_angle = (hour % 12) * 30 + minutes * 0.5

        # Difference between angles
        diff = abs(hour_angle - minute_angle)

        # Return smaller angle
        return min(diff, 360 - diff)


class SolutionVerbose:
    def angleClock(self, hour: int, minutes: int) -> float:
        """More explicit calculation"""
        # Convert hour to 0-11 range
        hour = hour % 12

        # Degrees per unit
        DEGREES_PER_HOUR = 30  # 360 / 12
        DEGREES_PER_MINUTE = 6  # 360 / 60
        HOUR_MOVE_PER_MINUTE = 0.5  # 30 / 60

        # Calculate angles
        hour_angle = hour * DEGREES_PER_HOUR + minutes * HOUR_MOVE_PER_MINUTE
        minute_angle = minutes * DEGREES_PER_MINUTE

        # Get absolute difference
        angle = abs(hour_angle - minute_angle)

        # Return smaller of two possible angles
        return min(angle, 360 - angle)
