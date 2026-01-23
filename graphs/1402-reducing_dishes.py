#1402. Reducing Dishes
#Hard
#
#A chef has collected data on the satisfaction level of his n dishes. Chef can
#cook any dish in 1 unit of time.
#
#Like-time coefficient of a dish is defined as the time taken to cook that dish
#including previous dishes multiplied by its satisfaction level i.e.
#time[i] * satisfaction[i].
#
#Return the maximum sum of like-time coefficient that the chef can obtain after
#dishes preparation.
#
#Dishes can be prepared in any order and the chef can discard some dishes to
#get this maximum value.
#
#Example 1:
#Input: satisfaction = [-1,-8,0,5,-9]
#Output: 14
#Explanation: After Removing the second and last dish, the maximum total
#like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
#Each dish is prepared in one unit of time.
#
#Example 2:
#Input: satisfaction = [4,3,2]
#Output: 20
#Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
#
#Example 3:
#Input: satisfaction = [-1,-4,-5]
#Output: 0
#Explanation: People do not like the dishes. No dish is prepared.
#
#Constraints:
#    n == satisfaction.length
#    1 <= n <= 500
#    -1000 <= satisfaction[i] <= 1000

from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        Greedy approach:
        1. Sort in descending order
        2. Add dishes one by one from highest satisfaction
        3. Stop when adding more dishes decreases total

        Key insight: When we add a dish at the beginning,
        - New dish contributes its value * 1
        - All existing dishes get +1 to their coefficient

        So adding dish with value v increases total by v + sum_of_existing.
        We keep adding while v + running_sum > 0.
        """
        satisfaction.sort(reverse=True)

        total = 0
        running_sum = 0

        for sat in satisfaction:
            running_sum += sat
            if running_sum > 0:
                total += running_sum
            else:
                break

        return total


class SolutionDP:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """DP approach: dp[i][j] = max coefficient using j dishes from first i"""
        n = len(satisfaction)
        satisfaction.sort()

        # dp[j] = max coefficient using exactly j dishes
        dp = [-float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            sat = satisfaction[i]
            # Process in reverse to avoid using same dish twice
            for j in range(i + 1, 0, -1):
                # Add sat at position j: contributes sat * j
                # But we need to add sat to all existing j-1 dishes' contribution
                dp[j] = max(dp[j], dp[j - 1] + sat * j)

        return max(dp)


class SolutionBruteOptimized:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        Sort ascending, try taking last k dishes for all k.
        If taking k dishes, coefficient = sum(satisfaction[-k+i] * (i+1))
        """
        satisfaction.sort()
        n = len(satisfaction)

        max_total = 0

        for k in range(1, n + 1):
            # Take last k dishes
            total = 0
            for i in range(k):
                total += satisfaction[n - k + i] * (i + 1)
            max_total = max(max_total, total)

        return max_total


class SolutionSimplified:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        Cleaner greedy: sort ascending, add from end while profitable.
        """
        satisfaction.sort()

        total = 0
        suffix_sum = 0

        # Iterate from end
        for i in range(len(satisfaction) - 1, -1, -1):
            suffix_sum += satisfaction[i]
            # Adding this dish increases total by suffix_sum
            # (its own contribution + pushes all others by 1)
            if suffix_sum > 0:
                total += suffix_sum
            else:
                break

        return total
