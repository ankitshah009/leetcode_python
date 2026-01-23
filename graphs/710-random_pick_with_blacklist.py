#710. Random Pick with Blacklist
#Hard
#
#You are given an integer n and an array of unique integers blacklist. Design
#an algorithm to pick a random integer in the range [0, n - 1] that is not in
#blacklist. Any integer that is in the mentioned range and not in blacklist
#should be equally likely to be returned.
#
#Optimize your algorithm such that it minimizes the number of calls to the
#built-in random function of your language.
#
#Implement the Solution class:
#- Solution(int n, int[] blacklist) Initializes the object with the integer n
#  and the blacklisted integers blacklist.
#- int pick() Returns a random integer in the range [0, n - 1] and not in
#  blacklist.
#
#Example 1:
#Input: ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
#       [[7, [2, 3, 5]], [], [], [], [], [], [], []]
#Output: [null, 0, 4, 1, 6, 1, 0, 4]
#Explanation:
#Solution solution = new Solution(7, [2, 3, 5]);
#solution.pick(); // return 0, 4, 1, 6, 0, or 4 randomly
#
#Constraints:
#    1 <= n <= 10^9
#    0 <= blacklist.length <= min(10^5, n - 1)
#    0 <= blacklist[i] < n
#    All the values of blacklist are unique.
#    At most 2 * 10^4 calls will be made to pick.

import random

class Solution:
    """
    Map blacklisted numbers in [0, m) to whitelist numbers in [m, n).
    Only need one random call per pick.
    """

    def __init__(self, n: int, blacklist: list[int]):
        self.m = n - len(blacklist)  # Valid range [0, m)

        blacklist_set = set(blacklist)

        # Find whitelist numbers in [m, n)
        whitelist_tail = []
        for i in range(self.m, n):
            if i not in blacklist_set:
                whitelist_tail.append(i)

        # Map blacklisted numbers in [0, m) to whitelist in [m, n)
        self.mapping = {}
        j = 0
        for b in blacklist:
            if b < self.m:
                self.mapping[b] = whitelist_tail[j]
                j += 1

    def pick(self) -> int:
        idx = random.randint(0, self.m - 1)
        return self.mapping.get(idx, idx)


class SolutionBinarySearch:
    """Binary search approach - counts blacklist elements before each point"""

    def __init__(self, n: int, blacklist: list[int]):
        self.n = n
        self.blacklist = sorted(blacklist)
        self.m = n - len(blacklist)

    def pick(self) -> int:
        # Pick random index in whitelist
        k = random.randint(0, self.m - 1)

        # Binary search to find actual number
        # k = actual_number - count of blacklist before it
        left, right = 0, self.n - 1

        while left < right:
            mid = (left + right) // 2
            # Count blacklist elements <= mid
            import bisect
            count = bisect.bisect_right(self.blacklist, mid)

            if mid - count < k:
                left = mid + 1
            else:
                right = mid

        return left


class SolutionSimple:
    """Simple approach for small n - store whitelist"""

    def __init__(self, n: int, blacklist: list[int]):
        blacklist_set = set(blacklist)
        self.whitelist = [i for i in range(n) if i not in blacklist_set]

    def pick(self) -> int:
        return random.choice(self.whitelist)
