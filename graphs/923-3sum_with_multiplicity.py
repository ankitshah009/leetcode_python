#923. 3Sum With Multiplicity
#Medium
#
#Given an integer array arr, and an integer target, return the number of tuples
#i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
#
#As the answer can be very large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
#Output: 20
#
#Example 2:
#Input: arr = [1,1,2,2,2,2], target = 5
#Output: 12
#
#Constraints:
#    3 <= arr.length <= 3000
#    0 <= arr[i] <= 100
#    0 <= target <= 300

from collections import Counter

class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        """
        Count occurrences and enumerate unique value combinations.
        """
        MOD = 10 ** 9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        result = 0

        for i, a in enumerate(keys):
            for j in range(i, len(keys)):
                b = keys[j]
                c = target - a - b

                if c < b:
                    continue
                if c not in count:
                    continue

                if a == b == c:
                    # Choose 3 from count[a]
                    n = count[a]
                    result += n * (n - 1) * (n - 2) // 6
                elif a == b:
                    # Choose 2 from count[a], 1 from count[c]
                    n = count[a]
                    result += n * (n - 1) // 2 * count[c]
                elif b == c:
                    # Choose 1 from count[a], 2 from count[b]
                    n = count[b]
                    result += count[a] * n * (n - 1) // 2
                else:
                    # All different
                    result += count[a] * count[b] * count[c]

                result %= MOD

        return result


class SolutionTwoSum:
    """Two sum approach"""

    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        count = Counter(arr)
        result = 0

        for a, cnt_a in count.items():
            for b, cnt_b in count.items():
                c = target - a - b
                if c not in count:
                    continue

                cnt_c = count[c]

                if a == b == c:
                    result += cnt_a * (cnt_a - 1) * (cnt_a - 2) // 6
                elif a == b:
                    result += cnt_a * (cnt_a - 1) // 2 * cnt_c
                elif a < b < c:
                    result += cnt_a * cnt_b * cnt_c

        return result % MOD


class SolutionSort:
    """Sort and two pointers"""

    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        n = len(arr)
        result = 0

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                total = arr[i] + arr[j] + arr[k]

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    if arr[j] == arr[k]:
                        count = k - j + 1
                        result += count * (count - 1) // 2
                        break
                    else:
                        left_count = 1
                        right_count = 1
                        while j + left_count < k and arr[j + left_count] == arr[j]:
                            left_count += 1
                        while k - right_count > j and arr[k - right_count] == arr[k]:
                            right_count += 1
                        result += left_count * right_count
                        j += left_count
                        k -= right_count

        return result % MOD
