#1360. Number of Days Between Two Dates
#Easy
#
#Write a program to count the number of days between two dates.
#
#The two dates are given as strings, their format is YYYY-MM-DD as shown in
#the examples.
#
#Example 1:
#Input: date1 = "2019-06-29", date2 = "2019-06-30"
#Output: 1
#
#Example 2:
#Input: date1 = "2020-01-15", date2 = "2019-12-31"
#Output: 15
#
#Constraints:
#    The given dates are valid dates between the years 1971 and 2100.

from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """Using datetime module"""
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)


class SolutionManual:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """Calculate days from year 0 for each date, then find difference"""

        def is_leap_year(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        def days_in_month(year, month):
            days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if month == 2 and is_leap_year(year):
                return 29
            return days[month]

        def days_from_epoch(date_str):
            year, month, day = map(int, date_str.split('-'))

            # Count days from year 1 to year-1
            total = 0
            for y in range(1, year):
                total += 366 if is_leap_year(y) else 365

            # Add days from months in current year
            for m in range(1, month):
                total += days_in_month(year, m)

            # Add remaining days
            total += day

            return total

        return abs(days_from_epoch(date1) - days_from_epoch(date2))


class SolutionOptimized:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """Optimized calculation without looping through years"""

        def is_leap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def days_since_1971(date_str):
            year, month, day = map(int, date_str.split('-'))

            # Days from 1971 to year-1
            days = 365 * (year - 1971)
            # Add leap days
            days += (year - 1) // 4 - 1970 // 4  # Leap years since 1971
            days -= (year - 1) // 100 - 1970 // 100
            days += (year - 1) // 400 - 1970 // 400

            # Days in months of current year
            month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            for m in range(1, month):
                days += month_days[m]

            # Add leap day if applicable
            if month > 2 and is_leap(year):
                days += 1

            days += day

            return days

        return abs(days_since_1971(date1) - days_since_1971(date2))
