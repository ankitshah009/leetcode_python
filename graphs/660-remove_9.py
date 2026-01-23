#660. Remove 9
#Hard
#
#Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...
#
#Now, you will have a new integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...].
#
#Given an integer n, return the n-th integer in the new sequence.
#
#Example 1:
#Input: n = 9
#Output: 10
#
#Example 2:
#Input: n = 10
#Output: 11
#
#Constraints:
#    1 <= n <= 8 × 10^8

class Solution:
    def newInteger(self, n: int) -> int:
        """
        The new sequence is essentially base-9 representation!
        Numbers without 9 form a base-9 system where digits are 0-8.
        Convert n to base 9.
        """
        result = 0
        base = 1

        while n > 0:
            result += (n % 9) * base
            n //= 9
            base *= 10

        return result


class SolutionRecursive:
    """Recursive base conversion"""

    def newInteger(self, n: int) -> int:
        if n == 0:
            return 0
        return self.newInteger(n // 9) * 10 + n % 9


class SolutionString:
    """Convert to base 9, interpret as decimal"""

    def newInteger(self, n: int) -> int:
        # Convert n to base 9 string
        if n == 0:
            return 0

        digits = []
        while n:
            digits.append(str(n % 9))
            n //= 9

        return int(''.join(reversed(digits)))


class SolutionBinarySearch:
    """Binary search approach (less efficient but educational)"""

    def newInteger(self, n: int) -> int:
        def count_without_9(x):
            """Count numbers from 1 to x that don't contain 9"""
            if x <= 0:
                return 0

            s = str(x)
            length = len(s)

            # dp approach for digit counting
            count = 0

            for i, digit in enumerate(s):
                d = int(digit)
                remaining = length - i - 1

                # Numbers with smaller digit at position i
                valid_digits = min(d, 9)  # 0-8 are valid (d choices if d <= 8)
                if d > 9:
                    valid_digits = 9

                if i == 0:
                    valid_digits = min(d, 9) - 1 if d > 0 else 0
                    count += valid_digits * (9 ** remaining)
                else:
                    count += min(d, 9) * (9 ** remaining)

                if d == 9:
                    break
            else:
                if '9' not in s:
                    count += 1

            return count

        # Binary search for the answer
        left, right = n, n * 2

        while left < right:
            mid = (left + right) // 2
            if count_without_9(mid) < n:
                left = mid + 1
            else:
                right = mid

        return left
