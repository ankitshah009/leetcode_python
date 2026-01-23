#1538. Guess the Majority in a Hidden Array
#Medium
#
#We have an integer array nums, where all the integers in nums are 0 or 1. You
#will not be given direct access to the array, instead, you will have an API
#ArrayReader which have the following functions:
#
#- int query(int a, int b, int c, int d): where 0 <= a < b < c < d < ArrayReader.length().
#  Returns:
#  - 1 if nums[a] + nums[b] > nums[c] + nums[d]
#  - 0 if nums[a] + nums[b] == nums[c] + nums[d]
#  - -1 if nums[a] + nums[b] < nums[c] + nums[d]
#- int length(): Returns the size of the array.
#
#You are allowed to call query() 2 * n times at most where n is equal to
#ArrayReader.length().
#
#Return any index of the most frequent element in nums. If there is a tie,
#return -1.
#
#Example 1:
#Input: nums = [0,0,1,0,1,1,1,1]
#Output: 5
#Explanation: The indices 5, 6, 7 correspond to value 1. Index 5 is returned.
#
#Example 2:
#Input: nums = [0,0,1,1,0]
#Output: 0
#
#Example 3:
#Input: nums = [1,0,1,0,1,0,1,0]
#Output: -1
#
#Constraints:
#    5 <= nums.length <= 10^5
#    0 <= nums[i] <= 1

class ArrayReader:
    """Mock API class for testing"""
    def __init__(self, nums):
        self.nums = nums

    def query(self, a: int, b: int, c: int, d: int) -> int:
        sum1 = self.nums[a] + self.nums[b]
        sum2 = self.nums[c] + self.nums[d]
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return -1
        return 0

    def length(self) -> int:
        return len(self.nums)


class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        """
        Key insight: Compare elements relative to arr[0].

        Use query(0,1,2,3) and variations to determine if elements
        are same or different from arr[0].

        If query(0,1,2,3) == query(0,1,2,i) then arr[3] == arr[i]
        (since positions 0,1,2 are fixed)
        """
        n = reader.length()

        # Determine relationships relative to arr[0]
        # same_count = elements equal to arr[0]
        # diff_count = elements different from arr[0]

        same_count = 1  # arr[0] is same as itself
        diff_count = 0
        diff_index = -1

        # Compare arr[0] vs arr[1] using query(0,2,3,4) vs query(1,2,3,4)
        # If equal, arr[0] == arr[1]
        q0234 = reader.query(0, 2, 3, 4)
        q1234 = reader.query(1, 2, 3, 4)

        if q0234 == q1234:
            same_count += 1
        else:
            diff_count += 1
            diff_index = 1

        # Compare arr[0] vs arr[2] using query(0,1,3,4) vs query(2,1,3,4)
        q0134 = reader.query(0, 1, 3, 4)
        q1234_sorted = reader.query(1, 2, 3, 4)  # This is same as q1234

        # Actually use query(0,3,1,4) vs query(2,3,1,4)
        # Or more simply: query(0,1,3,4) vs query(1,2,3,4)
        # If arr[0]==arr[2]: query(0,1,3,4) == query(1,2,3,4)

        # Let's use a cleaner approach:
        # query(0,1,2,3) as baseline
        q0123 = reader.query(0, 1, 2, 3)

        # For i >= 4: query(0,1,2,i) tells us if arr[i] == arr[3]
        # (since 0,1,2 are fixed, only 3 vs i matters)

        # First determine arr[2] vs arr[0]
        # Use query(0,2,3,4) vs query(1,2,3,4) - if equal, arr[0]==arr[1]
        # Use query(0,1,3,4) vs query(2,1,3,4) - wait, need 4 distinct indices

        # Simpler: compare query(0,1,2,3) vs query(0,1,2,4) to see if arr[3]==arr[4]
        # Then query(0,1,3,4) vs query(0,2,3,4) to see if arr[1]==arr[2]

        # Let me restart with a cleaner approach
        pass


class SolutionClean:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        """
        Compare all elements to arr[0].
        """
        n = reader.length()

        # q0123 is our reference
        q0123 = reader.query(0, 1, 2, 3)

        # same = count of elements equal to arr[0]
        # diff = count of elements different from arr[0]
        same_count = 1
        diff_count = 0
        diff_idx = -1
        same_idx = 0

        # For element 1: compare query(0,2,3,4) vs query(1,2,3,4)
        if n > 4:
            q0234 = reader.query(0, 2, 3, 4)
            q1234 = reader.query(1, 2, 3, 4)
            if q0234 == q1234:
                same_count += 1
            else:
                diff_count += 1
                diff_idx = 1
        else:
            # n == 5, use different queries
            q0134 = reader.query(0, 1, 3, 4)
            q0234 = reader.query(0, 2, 3, 4)
            if q0134 == q0234:
                same_count += 1
            else:
                diff_count += 1
                diff_idx = 1

        # For element 2: compare query(0,1,3,4) vs query(0,2,3,4)
        q0134 = reader.query(0, 1, 3, 4)
        q0234 = reader.query(0, 2, 3, 4)
        if q0134 == q0234:
            same_count += 1
        else:
            diff_count += 1
            diff_idx = 2

        # For element 3: compare query(0,1,2,4) vs query(0,1,3,4)
        q0124 = reader.query(0, 1, 2, 4)
        if q0124 == q0134:
            same_count += 1
        else:
            diff_count += 1
            diff_idx = 3

        # For elements 4 to n-1: compare query(0,1,2,3) vs query(0,1,2,i)
        for i in range(4, n):
            q012i = reader.query(0, 1, 2, i)
            if q0123 == q012i:
                # arr[i] == arr[3]
                # Need to know if arr[3] == arr[0]
                pass

        # Actually, let's track if arr[3] same as arr[0]
        arr3_same_as_0 = (q0124 == q0134)

        for i in range(4, n):
            q012i = reader.query(0, 1, 2, i)
            i_same_as_3 = (q012i == q0123)

            if i_same_as_3 == arr3_same_as_0:
                # arr[i] same as arr[0]
                same_count += 1
                same_idx = i
            else:
                diff_count += 1
                diff_idx = i

        if same_count > diff_count:
            return same_idx
        elif diff_count > same_count:
            return diff_idx
        else:
            return -1
