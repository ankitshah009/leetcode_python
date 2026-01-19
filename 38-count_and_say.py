#38. Count and Say
#Medium
#
#The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#    countAndSay(1) = "1"
#    countAndSay(n) is the run-length encoding of countAndSay(n - 1).
#
#Run-length encoding (RLE) is a string compression method that works by replacing consecutive
#identical characters with the character count followed by the character.
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
