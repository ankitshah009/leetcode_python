#170. Two Sum III - Data structure design
#Easy
#
#Design a data structure that accepts a stream of integers and checks if it has
#a pair of integers that sum up to a particular value.
#
#Implement the TwoSum class:
#    TwoSum() Initializes the TwoSum object, with an empty array initially.
#    void add(int number) Adds number to the data structure.
#    boolean find(int value) Returns true if there exists any pair of numbers
#    whose sum is equal to value, otherwise, returns false.
#
#Example 1:
#Input
#["TwoSum", "add", "add", "add", "find", "find"]
#[[], [1], [3], [5], [4], [7]]
#Output
#[null, null, null, null, true, false]
#
#Explanation
#TwoSum twoSum = new TwoSum();
#twoSum.add(1);   // [] --> [1]
#twoSum.add(3);   // [1] --> [1,3]
#twoSum.add(5);   // [1,3] --> [1,3,5]
#twoSum.find(4);  // 1 + 3 = 4, return true
#twoSum.find(7);  // No two integers sum up to 7, return false
#
#Constraints:
#    -10^5 <= number <= 10^5
#    -2^31 <= value <= 2^31 - 1
#    At most 5 * 10^4 calls will be made to add and find.

from collections import defaultdict

class TwoSum:
    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        for num in self.nums:
            complement = value - num
            if complement in self.nums:
                # Handle case where complement is same as num
                if complement != num or self.nums[num] > 1:
                    return True
        return False


class TwoSumOptimizedFind:
    """Optimized for frequent find operations"""

    def __init__(self):
        self.nums = []
        self.num_set = set()
        self.sum_set = set()

    def add(self, number: int) -> None:
        # Compute all new sums
        for num in self.nums:
            self.sum_set.add(num + number)

        self.nums.append(number)
        self.num_set.add(number)

    def find(self, value: int) -> bool:
        return value in self.sum_set


class TwoSumSortedList:
    """Using sorted list for balanced operations"""

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        import bisect
        bisect.insort(self.nums, number)

    def find(self, value: int) -> bool:
        left, right = 0, len(self.nums) - 1

        while left < right:
            curr_sum = self.nums[left] + self.nums[right]
            if curr_sum == value:
                return True
            elif curr_sum < value:
                left += 1
            else:
                right -= 1

        return False
