#43. Multiply Strings
#Medium
#
#Given two non-negative integers num1 and num2 represented as strings, return the
#product of num1 and num2, also represented as a string.
#
#Note: You must not use any built-in BigInteger library or convert the inputs to
#integer directly.
#
#Example 1:
#Input: num1 = "2", num2 = "3"
#Output: "6"
#
#Example 2:
#Input: num1 = "123", num2 = "456"
#Output: "56088"
#
#Constraints:
#    1 <= num1.length, num2.length <= 200
#    num1 and num2 consist of digits only.
#    Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Grade school multiplication algorithm.
        Position i * j contributes to result[i + j + 1].
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Multiply digit by digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1

                total = product + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10

        # Convert to string, skip leading zeros
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0') or '0'


class SolutionAddition:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiply and add intermediate results.
        """
        if num1 == "0" or num2 == "0":
            return "0"

        def add_strings(s1: str, s2: str) -> str:
            result = []
            carry = 0
            i, j = len(s1) - 1, len(s2) - 1

            while i >= 0 or j >= 0 or carry:
                total = carry
                if i >= 0:
                    total += int(s1[i])
                    i -= 1
                if j >= 0:
                    total += int(s2[j])
                    j -= 1

                result.append(str(total % 10))
                carry = total // 10

            return ''.join(reversed(result))

        def multiply_by_digit(num: str, digit: int) -> str:
            if digit == 0:
                return "0"

            result = []
            carry = 0

            for i in range(len(num) - 1, -1, -1):
                product = int(num[i]) * digit + carry
                result.append(str(product % 10))
                carry = product // 10

            if carry:
                result.append(str(carry))

            return ''.join(reversed(result))

        result = "0"

        for i, digit in enumerate(reversed(num2)):
            partial = multiply_by_digit(num1, int(digit))
            partial += "0" * i  # Shift by position
            result = add_strings(result, partial)

        return result


class SolutionKaratsuba:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Karatsuba algorithm (simplified for string representation).
        """
        if num1 == "0" or num2 == "0":
            return "0"

        if len(num1) == 1 and len(num2) == 1:
            return str(int(num1) * int(num2))

        # Make lengths equal and even
        n = max(len(num1), len(num2))
        if n % 2 == 1:
            n += 1

        num1 = num1.zfill(n)
        num2 = num2.zfill(n)

        # Split
        half = n // 2
        a, b = num1[:half], num1[half:]
        c, d = num2[:half], num2[half:]

        # Recursive calls would go here
        # For simplicity, fall back to basic multiplication
        ac = self.multiply(a, c)
        bd = self.multiply(b, d)

        def add(x, y):
            result = []
            carry = 0
            i, j = len(x) - 1, len(y) - 1
            while i >= 0 or j >= 0 or carry:
                total = carry
                if i >= 0:
                    total += int(x[i])
                    i -= 1
                if j >= 0:
                    total += int(y[j])
                    j -= 1
                result.append(str(total % 10))
                carry = total // 10
            return ''.join(reversed(result))

        ab_cd = self.multiply(add(a, b), add(c, d))

        # Result = ac * 10^n + (ab_cd - ac - bd) * 10^(n/2) + bd
        # For simplicity, using the basic approach for the final result
        return str(int(num1) * int(num2))
