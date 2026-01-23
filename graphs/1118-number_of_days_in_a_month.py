#1118. Number of Days in a Month
#Easy
#
#Given a year year and a month month, return the number of days of that month.
#
#Example 1:
#Input: year = 1992, month = 7
#Output: 31
#
#Example 2:
#Input: year = 2000, month = 2
#Output: 29
#
#Example 3:
#Input: year = 1900, month = 2
#Output: 28
#
#Constraints:
#    1583 <= year <= 2100
#    1 <= month <= 12

class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        """
        Check for leap year for February, otherwise use standard days.
        """
        # Days in each month (non-leap year)
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def is_leap_year(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        if month == 2 and is_leap_year(year):
            return 29

        return days_in_month[month]


class SolutionCalendar:
    def numberOfDays(self, year: int, month: int) -> int:
        """Using calendar module"""
        import calendar
        return calendar.monthrange(year, month)[1]


class SolutionDatetime:
    def numberOfDays(self, year: int, month: int) -> int:
        """Using datetime"""
        from datetime import date

        if month == 12:
            next_month = date(year + 1, 1, 1)
        else:
            next_month = date(year, month + 1, 1)

        this_month = date(year, month, 1)
        return (next_month - this_month).days
