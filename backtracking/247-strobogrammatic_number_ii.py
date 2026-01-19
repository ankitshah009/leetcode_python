#247. Strobogrammatic Number II
#Medium
#
#Given an integer n, return all the strobogrammatic numbers that are of length n.
#You may return the answer in any order.
#
#A strobogrammatic number is a number that looks the same when rotated 180 degrees
#(looked at upside down).
#
#Example 1:
#Input: n = 2
#Output: ["11","69","88","96"]
#
#Example 2:
#Input: n = 1
#Output: ["0","1","8"]
#
#Constraints:
#    1 <= n <= 14

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Strobogrammatic pairs: (0,0), (1,1), (6,9), (8,8), (9,6)
        # For middle digit (odd length): 0, 1, 8

        def helper(length, is_outermost):
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]

            # Build from center outward
            middles = helper(length - 2, False)
            result = []

            for middle in middles:
                for pair in [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]:
                    # Skip leading zeros for outermost layer
                    if is_outermost and pair[0] == "0":
                        continue
                    result.append(pair[0] + middle + pair[1])

            return result

        return helper(n, n > 1)

    # Iterative approach
    def findStrobogrammaticIterative(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        # Start from center and build outward
        if n % 2 == 0:
            result = [""]
        else:
            result = ["0", "1", "8"]

        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

        # Add pairs from center to outside
        remaining = n // 2
        for i in range(remaining):
            new_result = []
            for s in result:
                for left, right in pairs:
                    # Skip leading zeros except for innermost
                    if i == remaining - 1 and left == "0":
                        continue
                    new_result.append(left + s + right)
            result = new_result

        return result
