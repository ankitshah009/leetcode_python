#860. Lemonade Change
#Easy
#
#At a lemonade stand, each lemonade costs $5. Customers are standing in a queue
#to buy from you and order one at a time (in the order specified by bills).
#Each customer will only buy one lemonade and pay with either a $5, $10, or $20
#bill. You must provide the correct change to each customer so that the net
#transaction is that the customer pays $5.
#
#Note that you do not have any change in hand at first.
#
#Given an integer array bills where bills[i] is the bill the ith customer pays,
#return true if you can provide every customer with the correct change, or false
#otherwise.
#
#Example 1:
#Input: bills = [5,5,5,10,20]
#Output: true
#
#Example 2:
#Input: bills = [5,5,10,10,20]
#Output: false
#Explanation: We can not provide change for two $20 bills.
#
#Constraints:
#    1 <= bills.length <= 10^5
#    bills[i] is either 5, 10, or 20.

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        """
        Greedy: track $5 and $10 bills.
        For $20, prefer giving $10 + $5 over three $5s.
        """
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True


class SolutionDict:
    """Using dictionary to track bills"""

    def lemonadeChange(self, bills: list[int]) -> bool:
        change = {5: 0, 10: 0}

        for bill in bills:
            change[5] += 1  # Receive $5 for lemonade

            # Give change
            to_give = bill - 5

            if to_give == 15:
                if change[10] > 0:
                    change[10] -= 1
                    to_give -= 10
                while to_give > 0 and change[5] > 0:
                    change[5] -= 1
                    to_give -= 5
            elif to_give == 5:
                if change[5] > 0:
                    change[5] -= 1
                    to_give = 0

            if to_give > 0:
                return False

        return True


class SolutionSimple:
    """Simplified greedy"""

    def lemonadeChange(self, bills: list[int]) -> bool:
        fives = tens = 0

        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                fives, tens = fives - 1, tens + 1
            elif tens > 0:
                fives, tens = fives - 1, tens - 1
            else:
                fives -= 3

            if fives < 0:
                return False

        return True
