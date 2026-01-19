#528. Random Pick with Weight
#Medium
#
#You are given a 0-indexed array of positive integers w where w[i] describes the weight of the
#ith index.
#
#You need to implement the function pickIndex(), which randomly picks an index in the range
#[0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is
#w[i] / sum(w).
#
#Example 1:
#Input: ["Solution","pickIndex"]
#       [[[1]],[]]
#Output: [null,0]
#Explanation: Solution solution = new Solution([1]);
#solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
#
#Example 2:
#Input: ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
#       [[[1,3]],[],[],[],[],[]]
#Output: [null,1,1,1,1,0]
#Explanation: Solution solution = new Solution([1, 3]);
#solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
#
#Constraints:
#    1 <= w.length <= 10^4
#    1 <= w[i] <= 10^5
#    pickIndex will be called at most 10^4 times.

import random
import bisect

class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix_sum, target)
