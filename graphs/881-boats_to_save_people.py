#881. Boats to Save People
#Medium
#
#You are given an array people where people[i] is the weight of the ith person,
#and an infinite number of boats where each boat can carry a maximum weight of limit.
#
#Each boat carries at most two people at the same time, provided the sum of the
#weight of those people is at most limit.
#
#Return the minimum number of boats to carry every given person.
#
#Example 1:
#Input: people = [1,2], limit = 3
#Output: 1
#Explanation: 1 boat (1, 2)
#
#Example 2:
#Input: people = [3,2,2,1], limit = 3
#Output: 3
#Explanation: 3 boats (1, 2), (2) and (3)
#
#Example 3:
#Input: people = [3,5,3,4], limit = 5
#Output: 4
#Explanation: 4 boats (3), (3), (4), (5)
#
#Constraints:
#    1 <= people.length <= 5 * 10^4
#    1 <= people[i] <= limit <= 3 * 10^4

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        Greedy two-pointer: pair heaviest with lightest if possible.
        """
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1

        return boats


class SolutionExplained:
    """With explanation"""

    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        Greedy approach:
        1. Sort people by weight
        2. Try to pair heaviest person with lightest person
        3. If they fit together, both go in one boat
        4. If not, heaviest goes alone
        """
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0

        while i <= j:
            # Heaviest person always gets on a boat
            boats += 1

            # Can lightest join?
            if people[i] + people[j] <= limit:
                i += 1

            j -= 1

        return boats


class SolutionCounter:
    """Using counter for specific weight distributions"""

    def numRescueBoats(self, people: list[int], limit: int) -> int:
        from collections import Counter

        count = Counter(people)
        weights = sorted(count.keys())

        boats = 0
        left, right = 0, len(weights) - 1

        while left <= right:
            if left == right:
                # Same weight
                w = weights[left]
                if 2 * w <= limit:
                    # Pair them up
                    boats += (count[w] + 1) // 2
                else:
                    boats += count[w]
                break

            light, heavy = weights[left], weights[right]

            if light + heavy <= limit:
                # Pair light with heavy
                pairs = min(count[light], count[heavy])
                boats += pairs
                count[light] -= pairs
                count[heavy] -= pairs

            # Handle remaining heavy people
            if count[heavy] > 0:
                boats += count[heavy]
                count[heavy] = 0
                right -= 1
            else:
                right -= 1

            if count[light] == 0:
                left += 1

        return boats
