#400. Nth Digit
#Medium
#
#Given an integer n, return the nth digit of the infinite integer sequence
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
#
#Example 1:
#Input: n = 3
#Output: 3
#
#Example 2:
#Input: n = 11
#Output: 0
#Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
#... is a 0, which is part of the number 10.
#
#Constraints:
#    1 <= n <= 2^31 - 1

class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        Number ranges by digit count:
        - 1 digit: 1-9 (9 numbers, 9 digits)
        - 2 digits: 10-99 (90 numbers, 180 digits)
        - 3 digits: 100-999 (900 numbers, 2700 digits)
        - k digits: 10^(k-1) to 10^k - 1 (9*10^(k-1) numbers, k*9*10^(k-1) digits)
        """
        # Find which digit group n falls into
        digit_count = 1
        range_start = 1
        range_digits = 9

        while n > digit_count * range_digits:
            n -= digit_count * range_digits
            digit_count += 1
            range_start *= 10
            range_digits *= 10

        # Find the actual number
        # n-1 because we want 0-indexed position within this range
        number = range_start + (n - 1) // digit_count

        # Find which digit within the number
        digit_idx = (n - 1) % digit_count

        return int(str(number)[digit_idx])


class SolutionDetailed:
    """More detailed step-by-step solution"""

    def findNthDigit(self, n: int) -> int:
        # Step 1: Determine the length of the number containing the nth digit
        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Step 2: Determine the actual number
        # (n-1) // length gives how many numbers past 'start' we need to go
        number = start + (n - 1) // length

        # Step 3: Determine which digit of that number
        digit_index = (n - 1) % length

        # Step 4: Extract that digit
        return int(str(number)[digit_index])


class SolutionMath:
    """Pure math without string conversion"""

    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        number = start + (n - 1) // length
        digit_index = (n - 1) % length

        # Extract digit without string conversion
        # digit_index 0 = leftmost digit
        divisor = 10 ** (length - 1 - digit_index)
        return (number // divisor) % 10
