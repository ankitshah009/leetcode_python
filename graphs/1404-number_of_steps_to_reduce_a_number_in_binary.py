#1404. Number of Steps to Reduce a Number in Binary Representation to One
#Medium
#
#Given the binary representation of an integer as a string s, return the number
#of steps to reduce it to 1 under the following rules:
#    If the current number is even, you have to divide it by 2.
#    If the current number is odd, you have to add 1 to it.
#
#It is guaranteed that you can always reach one for all test cases.
#
#Example 1:
#Input: s = "1101"
#Output: 6
#Explanation: "1101" corressponds to number 13 in their decimal representation.
#Step 1) 13 is odd, add 1 and obtain 14.
#Step 2) 14 is even, divide by 2 and obtain 7.
#Step 3) 7 is odd, add 1 and obtain 8.
#Step 4) 8 is even, divide by 2 and obtain 4.
#Step 5) 4 is even, divide by 2 and obtain 2.
#Step 6) 2 is even, divide by 2 and obtain 1.
#
#Example 2:
#Input: s = "10"
#Output: 1
#Explanation: "10" corressponds to number 2 in their decimal representation.
#Step 1) 2 is even, divide by 2 and obtain 1.
#
#Example 3:
#Input: s = "1"
#Output: 0
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of characters '0' or '1'
#    s[0] == '1'

class Solution:
    def numSteps(self, s: str) -> int:
        """
        Simulate on binary string:
        - Even (ends in 0): remove last character (divide by 2)
        - Odd (ends in 1): add 1 (need to handle carry)
        """
        s = list(s)
        steps = 0

        while len(s) > 1:
            if s[-1] == '0':
                # Even: divide by 2
                s.pop()
            else:
                # Odd: add 1 (changes trailing 1s to 0s, flip next 0 to 1)
                # Find rightmost 0
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1

                if i >= 0:
                    s[i] = '1'
                else:
                    # All 1s, need to prepend 1
                    s.insert(0, '1')

            steps += 1

        return steps


class SolutionSimulateNumber:
    def numSteps(self, s: str) -> int:
        """Simulate with actual number (works for smaller inputs)"""
        num = int(s, 2)
        steps = 0

        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            steps += 1

        return steps


class SolutionOptimized:
    def numSteps(self, s: str) -> int:
        """
        Optimized approach:
        - Count trailing zeros (each is one divide operation)
        - Each 1 after that causes: add 1 + some divides
        - Handle carry propagation
        """
        steps = 0
        carry = 0

        # Process from right to left, skip the leading 1
        for i in range(len(s) - 1, 0, -1):
            digit = int(s[i]) + carry

            if digit == 0:
                # Even: one step (divide)
                steps += 1
            elif digit == 1:
                # Odd: add 1 (makes it even with carry), then divide
                steps += 2
                carry = 1
            else:  # digit == 2 (was 1 + carry)
                # Even: one step, carry continues
                steps += 1
                carry = 1

        # Handle carry at position 0
        steps += carry

        return steps


class SolutionClean:
    def numSteps(self, s: str) -> int:
        """Clean bit manipulation approach"""
        steps = 0
        carry = 0

        # Process from right, stop before leading bit
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit == 1:
                # Odd: add 1 (step), becomes even with carry, divide (step)
                steps += 2
                carry = 1
            else:
                # bit is 0 or 2 (even): just divide (step)
                steps += 1
                carry = 1 if bit == 2 else 0

        return steps + carry
