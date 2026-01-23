#1518. Water Bottles
#Easy
#
#There are numBottles water bottles that are initially full of water. You can
#exchange numExchange empty water bottles from the market with one full water
#bottle.
#
#The operation of drinking a full water bottle turns it into an empty bottle.
#
#Given the two integers numBottles and numExchange, return the maximum number
#of water bottles you can drink.
#
#Example 1:
#Input: numBottles = 9, numExchange = 3
#Output: 13
#Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
#Number of water bottles you can drink: 9 + 3 + 1 = 13.
#
#Example 2:
#Input: numBottles = 15, numExchange = 4
#Output: 19
#Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
#Number of water bottles you can drink: 15 + 3 + 1 = 19.
#
#Constraints:
#    1 <= numBottles <= 100
#    2 <= numExchange <= 100

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Simulate the process: drink all, exchange empties for new bottles.
        """
        total_drunk = 0
        empty = 0

        while numBottles > 0:
            # Drink all full bottles
            total_drunk += numBottles
            empty += numBottles

            # Exchange empties for new full bottles
            numBottles = empty // numExchange
            empty = empty % numExchange

        return total_drunk


class SolutionMath:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Mathematical solution.
        After drinking n bottles, we have n empties.
        n empties -> n // e new bottles (with n % e empties left)

        Total = n + floor((n-1) / (e-1))

        Proof: Each exchange "costs" (e-1) empties for 1 drink.
        We start with n, so we can do floor((n-1) / (e-1)) exchanges.
        """
        return numBottles + (numBottles - 1) // (numExchange - 1)


class SolutionRecursive:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """Recursive solution"""
        if numBottles < numExchange:
            return numBottles

        new_bottles = numBottles // numExchange
        leftover = numBottles % numExchange

        return numBottles + self.numWaterBottles(new_bottles + leftover, numExchange) - (new_bottles + leftover)


class SolutionIterative:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """Cleaner iterative"""
        total = numBottles
        empties = numBottles

        while empties >= numExchange:
            new_bottles = empties // numExchange
            empties = empties % numExchange + new_bottles
            total += new_bottles

        return total


class SolutionWhile:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """Simple while loop"""
        result = 0
        empty = 0

        while numBottles:
            result += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty %= numExchange

        return result
