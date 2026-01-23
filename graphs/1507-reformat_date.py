#1507. Reformat Date
#Easy
#
#Given a date string in the form Day Month Year, where:
#    Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
#    Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
#    "Sep", "Oct", "Nov", "Dec"}.
#    Year is in the range [1900, 2100].
#
#Convert the date string to the format YYYY-MM-DD, where:
#    YYYY denotes the 4 digit year.
#    MM denotes the 2 digit month.
#    DD denotes the 2 digit day.
#
#Example 1:
#Input: date = "20th Oct 2052"
#Output: "2052-10-20"
#
#Example 2:
#Input: date = "6th Jun 1933"
#Output: "1933-06-06"
#
#Example 3:
#Input: date = "26th May 1960"
#Output: "1960-05-26"
#
#Constraints:
#    The given dates are guaranteed to be valid, so no error handling is necessary.

class Solution:
    def reformatDate(self, date: str) -> str:
        """
        Parse day, month, year and format.
        """
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        parts = date.split()
        day_str = parts[0]
        month_str = parts[1]
        year_str = parts[2]

        # Extract day number (remove suffix)
        day = int(day_str[:-2])  # Remove 'st', 'nd', 'rd', 'th'

        # Get month number
        month = months[month_str]

        return f"{year_str}-{month}-{day:02d}"


class SolutionRegex:
    def reformatDate(self, date: str) -> str:
        """Using regex to extract day number"""
        import re

        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        # Extract numeric day
        day = int(re.findall(r'\d+', date)[0])

        parts = date.split()
        month = months[parts[1]]
        year = parts[2]

        return f"{year}-{month}-{day:02d}"


class SolutionDatetime:
    def reformatDate(self, date: str) -> str:
        """Using datetime for parsing"""
        from datetime import datetime

        # Remove ordinal suffix from day
        parts = date.split()
        day_num = ''.join(filter(str.isdigit, parts[0]))
        clean_date = f"{day_num} {parts[1]} {parts[2]}"

        dt = datetime.strptime(clean_date, "%d %b %Y")
        return dt.strftime("%Y-%m-%d")


class SolutionList:
    def reformatDate(self, date: str) -> str:
        """Using list index for month"""
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        parts = date.split()

        # Extract day
        day = int(''.join(c for c in parts[0] if c.isdigit()))

        # Get month index (1-based)
        month = months.index(parts[1]) + 1

        # Year
        year = parts[2]

        return f"{year}-{month:02d}-{day:02d}"


class SolutionCompact:
    def reformatDate(self, date: str) -> str:
        """Compact one-liner style"""
        m = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
             "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

        d, mon, y = date.split()
        return f"{y}-{m[mon]:02d}-{int(d[:-2]):02d}"
