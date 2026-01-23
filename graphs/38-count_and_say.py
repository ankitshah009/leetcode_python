#38. Count and Say
#Medium
#
#The count-and-say sequence is a sequence of digit strings defined by the
#recursive formula:
#- countAndSay(1) = "1"
#- countAndSay(n) is the run-length encoding of countAndSay(n - 1).
#
#Run-length encoding (RLE) is a string compression method that works by replacing
#consecutive identical characters with the count of those characters followed by
#the character itself.
#
#Example 1:
#Input: n = 4
#Output: "1211"
#Explanation:
#countAndSay(1) = "1"
#countAndSay(2) = RLE of "1" = "11"
#countAndSay(3) = RLE of "11" = "21"
#countAndSay(4) = RLE of "21" = "1211"
#
#Example 2:
#Input: n = 1
#Output: "1"
#
#Constraints:
#    1 <= n <= 30

class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Iterative approach - build sequence step by step.
        """
        result = "1"

        for _ in range(n - 1):
            new_result = []
            count = 1
            char = result[0]

            for i in range(1, len(result)):
                if result[i] == char:
                    count += 1
                else:
                    new_result.append(str(count) + char)
                    char = result[i]
                    count = 1

            new_result.append(str(count) + char)
            result = ''.join(new_result)

        return result


class SolutionRecursive:
    def countAndSay(self, n: int) -> str:
        """
        Recursive approach.
        """
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = []
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result.append(str(count) + prev[i - 1])
                count = 1

        result.append(str(count) + prev[-1])

        return ''.join(result)


class SolutionGroupBy:
    def countAndSay(self, n: int) -> str:
        """
        Using itertools.groupby.
        """
        from itertools import groupby

        result = "1"

        for _ in range(n - 1):
            result = ''.join(str(len(list(group))) + digit
                           for digit, group in groupby(result))

        return result


class SolutionRegex:
    def countAndSay(self, n: int) -> str:
        """
        Using regex for grouping consecutive characters.
        """
        import re

        result = "1"

        for _ in range(n - 1):
            result = re.sub(r'(.)\1*', lambda m: str(len(m.group())) + m.group(1), result)

        return result
