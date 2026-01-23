#1904. The Number of Full Rounds You Have Played
#Medium
#
#You are participating in an online chess tournament. There is a chess round
#that starts every 15 minutes. The first round of the day starts at 00:00, and
#after every 15 minutes, a new round starts.
#
#You are given two strings loginTime and logoutTime where:
#- loginTime is the time you will login to the game, and
#- logoutTime is the time you will logout from the game.
#
#If logoutTime is earlier than loginTime, this means you have played from
#loginTime to midnight and from midnight to logoutTime.
#
#Return the number of full chess rounds you have played in the tournament.
#
#Example 1:
#Input: loginTime = "09:31", logoutTime = "10:14"
#Output: 1
#
#Example 2:
#Input: loginTime = "21:30", logoutTime = "03:00"
#Output: 22
#
#Constraints:
#    loginTime and logoutTime are in the format hh:mm.
#    00 <= hh <= 23
#    00 <= mm <= 59
#    loginTime and logoutTime are not equal.

class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        """
        Convert to minutes, handle wrap-around, count 15-min intervals.
        """
        def to_minutes(time: str) -> int:
            h, m = map(int, time.split(':'))
            return h * 60 + m

        login = to_minutes(loginTime)
        logout = to_minutes(logoutTime)

        # Handle wrap-around (playing past midnight)
        if logout < login:
            logout += 24 * 60

        # Round login up to next 15-min boundary
        login_start = ((login + 14) // 15) * 15

        # Round logout down to previous 15-min boundary
        logout_end = (logout // 15) * 15

        # Count full rounds
        return max(0, (logout_end - login_start) // 15)


class SolutionDetailed:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        """
        Same logic with explicit steps.
        """
        login_h, login_m = map(int, loginTime.split(':'))
        logout_h, logout_m = map(int, logoutTime.split(':'))

        login_mins = login_h * 60 + login_m
        logout_mins = logout_h * 60 + logout_m

        # Handle midnight wrap
        if logout_mins < login_mins:
            logout_mins += 1440  # 24 * 60

        # Find first round start after login (ceil to 15)
        if login_mins % 15 != 0:
            login_mins = (login_mins // 15 + 1) * 15

        # Find last round end before logout (floor to 15)
        logout_mins = (logout_mins // 15) * 15

        return max(0, (logout_mins - login_mins) // 15)
