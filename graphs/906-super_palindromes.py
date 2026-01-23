#906. Super Palindromes
#Hard
#
#Let's say a positive integer is a super-palindrome if it is a palindrome, and
#it is also the square of a palindrome.
#
#Given two positive integers left and right represented as strings, return the
#number of super-palindromes in the inclusive range [left, right].
#
#Example 1:
#Input: left = "4", right = "1000"
#Output: 4
#Explanation: 4, 9, 121, 484 are super-palindromes.
#
#Example 2:
#Input: left = "1", right = "2"
#Output: 1
#
#Constraints:
#    1 <= left.length, right.length <= 18
#    left and right consist of only digits.
#    left and right cannot have leading zeros.
#    left and right represent integers in the range [1, 10^18].
#    left is less than or equal to right.

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        Generate palindrome roots and check if square is palindrome.
        """
        L, R = int(left), int(right)
        MAGIC = 100000  # sqrt(10^18) has at most 9 digits
        count = 0

        def is_palindrome(n: int) -> bool:
            s = str(n)
            return s == s[::-1]

        # Odd length palindromes: 1, 2, 3, ..., 121, 131, ...
        for k in range(MAGIC):
            s = str(k)
            root = int(s + s[-2::-1])  # Create palindrome
            square = root * root

            if square > R:
                break
            if square >= L and is_palindrome(square):
                count += 1

        # Even length palindromes: 11, 22, ..., 1111, 1221, ...
        for k in range(MAGIC):
            s = str(k)
            root = int(s + s[::-1])  # Create even palindrome
            square = root * root

            if square > R:
                break
            if square >= L and is_palindrome(square):
                count += 1

        return count


class SolutionAlternate:
    """Generate all palindromes up to sqrt(R)"""

    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        limit = int(R ** 0.5) + 1

        def is_palindrome(n: int) -> bool:
            s = str(n)
            return s == s[::-1]

        def generate_palindromes(max_val: int):
            palindromes = []
            # Single digit
            for i in range(1, 10):
                if i <= max_val:
                    palindromes.append(i)

            # Generate longer palindromes
            for length in range(2, 10):
                half_len = (length + 1) // 2
                start = 10 ** (half_len - 1)
                end = 10 ** half_len

                for half in range(start, end):
                    s = str(half)
                    if length % 2 == 0:
                        pal = int(s + s[::-1])
                    else:
                        pal = int(s + s[-2::-1])

                    if pal <= max_val:
                        palindromes.append(pal)

            return palindromes

        count = 0
        for p in generate_palindromes(limit):
            square = p * p
            if L <= square <= R and is_palindrome(square):
                count += 1

        return count
