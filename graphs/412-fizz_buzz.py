#412. Fizz Buzz
#Easy
#
#Given an integer n, return a string array answer (1-indexed) where:
#- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#- answer[i] == "Fizz" if i is divisible by 3.
#- answer[i] == "Buzz" if i is divisible by 5.
#- answer[i] == i (as a string) if none of the above conditions are true.
#
#Example 1:
#Input: n = 3
#Output: ["1","2","Fizz"]
#
#Example 2:
#Input: n = 5
#Output: ["1","2","Fizz","4","Buzz"]
#
#Example 3:
#Input: n = 15
#Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz",
#         "13","14","FizzBuzz"]
#
#Constraints:
#    1 <= n <= 10^4

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """Standard implementation"""
        result = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result


class SolutionConcatenation:
    """String concatenation approach - more flexible for adding conditions"""

    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"

            result.append(s if s else str(i))

        return result


class SolutionNoMod:
    """Without using modulo operator"""

    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        fizz = 0
        buzz = 0

        for i in range(1, n + 1):
            fizz += 1
            buzz += 1

            if fizz == 3 and buzz == 5:
                result.append("FizzBuzz")
                fizz = buzz = 0
            elif fizz == 3:
                result.append("Fizz")
                fizz = 0
            elif buzz == 5:
                result.append("Buzz")
                buzz = 0
            else:
                result.append(str(i))

        return result


class SolutionDict:
    """Dictionary approach - most extensible"""

    def fizzBuzz(self, n: int) -> List[str]:
        mappings = {3: "Fizz", 5: "Buzz"}

        result = []
        for i in range(1, n + 1):
            s = ""
            for divisor, word in mappings.items():
                if i % divisor == 0:
                    s += word
            result.append(s if s else str(i))

        return result
