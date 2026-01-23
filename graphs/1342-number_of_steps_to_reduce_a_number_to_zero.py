#1342. Number of Steps to Reduce a Number to Zero
#Easy
#
#Given an integer num, return the number of steps to reduce it to zero.
#
#In one step, if the current number is even, you have to divide it by 2,
#otherwise, you have to subtract 1 from it.
#
#Example 1:
#Input: num = 14
#Output: 6
#Explanation:
#Step 1) 14 is even; divide by 2 and obtain 7.
#Step 2) 7 is odd; subtract 1 and obtain 6.
#Step 3) 6 is even; divide by 2 and obtain 3.
#Step 4) 3 is odd; subtract 1 and obtain 2.
#Step 5) 2 is even; divide by 2 and obtain 1.
#Step 6) 1 is odd; subtract 1 and obtain 0.
#
#Example 2:
#Input: num = 8
#Output: 4
#Explanation:
#Step 1) 8 is even; divide by 2 and obtain 4.
#Step 2) 4 is even; divide by 2 and obtain 2.
#Step 3) 2 is even; divide by 2 and obtain 1.
#Step 4) 1 is odd; subtract 1 and obtain 0.
#
#Example 3:
#Input: num = 123
#Output: 12
#
#Constraints:
#    0 <= num <= 10^6

class Solution:
    def numberOfSteps(self, num: int) -> int:
        """Simple simulation."""
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps


class SolutionBitwise:
    def numberOfSteps(self, num: int) -> int:
        """
        Bitwise approach:
        - Even: right shift (divide by 2)
        - Odd: clear last bit (subtract 1)

        Steps = number of bits + number of 1 bits - 1 (for num > 0)
        """
        if num == 0:
            return 0

        steps = 0
        while num > 0:
            if num & 1:  # Odd
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps


class SolutionBitCount:
    def numberOfSteps(self, num: int) -> int:
        """
        Each bit takes 1 step to shift right.
        Each 1 bit takes 1 extra step to subtract.
        Total = bit_length + count_ones - 1 (for the final 1 becoming 0)
        """
        if num == 0:
            return 0

        return num.bit_length() + bin(num).count('1') - 1


class SolutionRecursive:
    def numberOfSteps(self, num: int) -> int:
        """Recursive approach"""
        if num == 0:
            return 0
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num // 2)
        return 1 + self.numberOfSteps(num - 1)
