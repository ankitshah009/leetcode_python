#1323. Maximum 69 Number
#Easy
#
#You are given a positive integer num consisting only of digits 6 and 9.
#
#Return the maximum number you can get by changing at most one digit (6 becomes
#9, and 9 becomes 6).
#
#Example 1:
#Input: num = 9669
#Output: 9969
#Explanation:
#Changing the first digit results in 6669.
#Changing the second digit results in 9969.
#Changing the third digit results in 9699.
#Changing the fourth digit results in 9666.
#The maximum number is 9969.
#
#Example 2:
#Input: num = 9996
#Output: 9999
#Explanation: Changing the last digit 6 to 9 results in the maximum number.
#
#Example 3:
#Input: num = 9999
#Output: 9999
#Explanation: It is better not to apply any change.
#
#Constraints:
#    1 <= num <= 10^4
#    num consists of only 6 and 9 digits.

class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        Change the leftmost 6 to 9.
        """
        s = str(num)
        idx = s.find('6')
        if idx == -1:
            return num
        return int(s[:idx] + '9' + s[idx + 1:])


class SolutionReplace:
    def maximum69Number(self, num: int) -> int:
        """Using string replace (replaces first occurrence only with count=1)"""
        return int(str(num).replace('6', '9', 1))


class SolutionMath:
    def maximum69Number(self, num: int) -> int:
        """Mathematical approach without string conversion"""
        # Find position of leftmost 6
        temp = num
        position = -1
        current_pos = 0

        while temp > 0:
            if temp % 10 == 6:
                position = current_pos
            temp //= 10
            current_pos += 1

        if position == -1:
            return num

        # Add 3 * 10^position to change 6 to 9
        return num + 3 * (10 ** position)
