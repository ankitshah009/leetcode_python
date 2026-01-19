#273. Integer to English Words
#Hard
#
#Convert a non-negative integer num to its English words representation.
#
#Example 1:
#Input: num = 123
#Output: "One Hundred Twenty Three"
#
#Example 2:
#Input: num = 12345
#Output: "Twelve Thousand Three Hundred Forty Five"
#
#Example 3:
#Input: num = 1234567
#Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
#Constraints:
#    0 <= num <= 2^31 - 1

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return ones[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return ones[n // 100] + " Hundred " + helper(n % 100)

        result = ""
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                result = helper(num % 1000) + unit + " " + result
            num //= 1000

        return result.strip()

    # Alternative iterative approach
    def numberToWordsIterative(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                    "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                "Seventy", "Eighty", "Ninety"]

        def two_digits(n):
            if n < 20:
                return below_20[n]
            elif n < 100:
                return tens[n // 10] + (" " + below_20[n % 10] if n % 10 else "")
            return ""

        def three_digits(n):
            if n < 100:
                return two_digits(n)
            else:
                hundred = below_20[n // 100] + " Hundred"
                remainder = n % 100
                return hundred + (" " + two_digits(remainder) if remainder else "")

        billions = num // 1000000000
        millions = (num % 1000000000) // 1000000
        thousands = (num % 1000000) // 1000
        remainder = num % 1000

        result = []
        if billions:
            result.append(three_digits(billions) + " Billion")
        if millions:
            result.append(three_digits(millions) + " Million")
        if thousands:
            result.append(three_digits(thousands) + " Thousand")
        if remainder:
            result.append(three_digits(remainder))

        return " ".join(result)
