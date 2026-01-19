#904. Fruit Into Baskets
#Medium
#
#You are visiting a farm that has a single row of fruit trees arranged from left
#to right. The trees are represented by an integer array fruits where fruits[i]
#is the type of fruit the ith tree produces.
#
#You want to collect as much fruit as possible. However, the owner has some strict
#rules that you must follow:
#
#You only have two baskets, and each basket can only hold a single type of fruit.
#There is no limit on the amount of fruit each basket can hold.
#Starting from any tree of your choice, you must pick exactly one fruit from every
#tree (including the start tree) while moving to the right. The picked fruits must
#fit in one of your baskets.
#Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
#
#Given the integer array fruits, return the maximum number of fruits you can pick.
#
#Example 1:
#Input: fruits = [1,2,1]
#Output: 3
#Explanation: We can pick from all 3 trees.
#
#Example 2:
#Input: fruits = [0,1,2,2]
#Output: 3
#Explanation: We can pick from trees [1,2,2]. If we had started at the first tree,
#we would only pick from trees [0,1].
#
#Example 3:
#Input: fruits = [1,2,3,2,2]
#Output: 4
#Explanation: We can pick from trees [2,3,2,2]. If we had started at the first tree,
#we would only pick from trees [1,2].
#
#Constraints:
#    1 <= fruits.length <= 10^5
#    0 <= fruits[i] < fruits.length

from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Sliding window - longest subarray with at most 2 distinct elements.
        """
        count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


class SolutionOptimized:
    """Optimized - window never shrinks"""

    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

        return len(fruits) - left


class SolutionTwoPointers:
    """Track last two fruit types explicitly"""

    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0
        curr_max = 0

        for fruit in fruits:
            if fruit == last_fruit or fruit == second_last_fruit:
                curr_max += 1
            else:
                curr_max = last_fruit_count + 1

            if fruit == last_fruit:
                last_fruit_count += 1
            else:
                last_fruit_count = 1

            if fruit != last_fruit:
                second_last_fruit = last_fruit
                last_fruit = fruit

            max_fruits = max(max_fruits, curr_max)

        return max_fruits
