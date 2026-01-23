#1154. Day of the Year
#Easy
#
#Given a string date representing a Gregorian calendar date formatted as
#YYYY-MM-DD, return the day number of the year.
#
#Example 1:
#Input: date = "2019-01-09"
#Output: 9
#Explanation: Given date is the 9th day of the year in 2019.
#
#Example 2:
#Input: date = "2019-02-10"
#Output: 41
#
#Constraints:
#    date.length == 10
#    date[4] == date[7] == '-'
#    date represents a calendar date between Jan 1st, 1900 and Dec 31st, 2019.

class Solution:
    def dayOfYear(self, date: str) -> int:
        """Calculate day of year considering leap years"""
        year, month, day = map(int, date.split('-'))

        # Days in each month (non-leap year)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Check leap year
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            days_in_month[1] = 29

        # Sum days of previous months + current day
        return sum(days_in_month[:month - 1]) + day


class SolutionPrefixSum:
    def dayOfYear(self, date: str) -> int:
        """Using prefix sum for months"""
        year, month, day = map(int, date.split('-'))

        # Prefix sum of days (index = month number)
        # prefix[i] = days before month i
        prefix = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        result = prefix[month] + day

        # Add 1 if leap year and month > February
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap and month > 2:
            result += 1

        return result


class SolutionDatetime:
    def dayOfYear(self, date: str) -> int:
        """Using datetime library"""
        from datetime import datetime
        dt = datetime.strptime(date, "%Y-%m-%d")
        return dt.timetuple().tm_yday
