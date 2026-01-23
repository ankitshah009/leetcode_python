#1103. Distribute Candies to People
#Easy
#
#We distribute some number of candies, to a row of n = num_people people in
#the following way:
#
#We then give 1 candy to the first person, 2 candies to the second person,
#and so on until we give n candies to the last person.
#
#Then, we go back to the start of the row, giving n + 1 candies to the first
#person, n + 2 candies to the second person, and so on until we give 2 * n
#candies to the last person.
#
#This process repeats (with us giving one more candy each time, and moving
#to the start of the row after we reach the end) until we run out of candies.
#The last person will receive all of our remaining candies (not necessarily
#one more than the previous gift).
#
#Return an array (of length num_people and sum candies) that represents the
#final distribution of candies.
#
#Example 1:
#Input: candies = 7, num_people = 4
#Output: [1,2,3,1]
#Explanation:
#On the first turn, ans[0] += 1, and the array is [1,0,0,0].
#On the second turn, ans[1] += 2, and the array is [1,2,0,0].
#On the third turn, ans[2] += 3, and the array is [1,2,3,0].
#On the fourth turn, ans[3] += 1 (because there is only one candy left), and
#the final array is [1,2,3,1].
#
#Example 2:
#Input: candies = 10, num_people = 3
#Output: [5,2,3]
#Explanation:
#On the first turn, ans[0] += 1, and the array is [1,0,0].
#On the second turn, ans[1] += 2, and the array is [1,2,0].
#On the third turn, ans[2] += 3, and the array is [1,2,3].
#On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
#
#Constraints:
#    1 <= candies <= 10^9
#    1 <= num_people <= 1000

from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """
        Simulation: Give candies round by round.
        """
        result = [0] * num_people
        give = 1

        while candies > 0:
            for i in range(num_people):
                if candies <= 0:
                    break
                actual = min(give, candies)
                result[i] += actual
                candies -= actual
                give += 1

        return result


class SolutionMath:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """
        Mathematical approach: Find complete rounds, then distribute remainder.
        """
        n = num_people

        # Find number of complete distributions
        # Sum of 1+2+...+k = k*(k+1)/2 <= candies
        # Find largest k such that k*(k+1)/2 <= candies
        k = int((2 * candies + 0.25) ** 0.5 - 0.5)
        while k * (k + 1) // 2 > candies:
            k -= 1

        remainder = candies - k * (k + 1) // 2
        complete_rounds = k // n

        result = [0] * n

        for i in range(n):
            # How many times did person i get candies in complete rounds?
            gifts = k // n + (1 if i < k % n else 0)

            if gifts == 0:
                continue

            # Person i gets: (i+1), (i+1+n), (i+1+2n), ...
            # This is arithmetic series with first term (i+1), common diff n
            # Sum = gifts * (i+1) + n * (0 + 1 + ... + (gifts-1))
            #     = gifts * (i+1) + n * gifts * (gifts-1) / 2
            result[i] = gifts * (i + 1) + n * gifts * (gifts - 1) // 2

        # Distribute remainder to person k % n
        if remainder > 0:
            result[k % n] += remainder

        return result


class SolutionCompact:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """Compact simulation"""
        result = [0] * num_people
        i = 0
        while candies > 0:
            result[i % num_people] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return result
