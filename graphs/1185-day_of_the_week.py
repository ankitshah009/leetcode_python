#1185. Day of the Week
#Easy
#
#Given a date, return the corresponding day of the week for that date.
#
#The input is given as three integers representing the day, month and year
#respectively.
#
#Return the answer as one of the following values {"Sunday", "Monday",
#"Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
#
#Example 1:
#Input: day = 31, month = 8, year = 2019
#Output: "Saturday"
#
#Example 2:
#Input: day = 18, month = 7, year = 1999
#Output: "Sunday"
#
#Example 3:
#Input: day = 15, month = 8, year = 1993
#Output: "Sunday"
#
#Constraints:
#    The given dates are valid dates between the years 1971 and 2100.

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """
        Zeller's formula for day of week.
        """
        days = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]

        # Adjust for Zeller's formula (Jan and Feb are months 13, 14 of previous year)
        if month < 3:
            month += 12
            year -= 1

        q = day
        m = month
        k = year % 100  # Year of century
        j = year // 100  # Century

        # Zeller's formula
        h = (q + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7

        # h: 0 = Saturday, 1 = Sunday, 2 = Monday, ...
        day_index = (h + 6) % 7

        return days[day_index]


class SolutionDatetime:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """Using datetime library"""
        import datetime

        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]

        d = datetime.date(year, month, day)
        return days[d.weekday()]


class SolutionCounting:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """Count days from a known reference date"""
        days = ["Thursday", "Friday", "Saturday", "Sunday",
                "Monday", "Tuesday", "Wednesday"]

        # Reference: Jan 1, 1971 was Friday, so we use index 0 = Thursday
        # Actually Jan 1, 1970 was Thursday
        # Let's use Jan 1, 1971 which was Friday

        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        def days_in_month(m, y):
            if m in [1, 3, 5, 7, 8, 10, 12]:
                return 31
            elif m in [4, 6, 9, 11]:
                return 30
            else:  # February
                return 29 if is_leap(y) else 28

        # Count days from Jan 1, 1971
        total_days = 0

        # Add days for complete years
        for y in range(1971, year):
            total_days += 366 if is_leap(y) else 365

        # Add days for complete months
        for m in range(1, month):
            total_days += days_in_month(m, year)

        # Add remaining days
        total_days += day

        # Jan 1, 1971 was Friday (index 1 in our array starting with Thursday)
        return days[total_days % 7]
