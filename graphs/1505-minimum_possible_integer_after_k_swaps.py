#1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits
#Hard
#
#You are given a string num representing the digits of a very large integer and
#an integer k. You are allowed to swap any two adjacent digits of the integer
#at most k times.
#
#Return the minimum integer you can obtain also as a string.
#
#Example 1:
#Input: num = "4321", k = 4
#Output: "1342"
#Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent
#swaps are shown.
#4321 -> 3421 -> 3412 -> 3142 -> 1342
#
#Example 2:
#Input: num = "100", k = 1
#Output: "010"
#Explanation: It's ok for the output to have leading zeros, but the input is
#guaranteed not to have any leading zeros.
#
#Example 3:
#Input: num = "36789", k = 1000
#Output: "36789"
#Explanation: We can keep the number without any swaps.
#
#Constraints:
#    1 <= num.length <= 30000
#    num contains only digits and doesn't have leading zeros.
#    1 <= k <= 10^9

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        """
        Greedy: at each position, bring the smallest digit possible
        (that can be reached with remaining k swaps) to the front.
        Use BIT to track actual positions after previous swaps.
        """
        from collections import deque

        n = len(num)
        if k >= n * (n - 1) // 2:
            # Can sort completely
            return ''.join(sorted(num))

        # Queues for positions of each digit
        digit_positions = [deque() for _ in range(10)]
        for i, ch in enumerate(num):
            digit_positions[int(ch)].append(i)

        # Binary Indexed Tree to track number of elements removed before position
        bit = [0] * (n + 1)

        def update(i: int, delta: int = 1) -> None:
            i += 1  # 1-indexed
            while i <= n:
                bit[i] += delta
                i += i & (-i)

        def query(i: int) -> int:
            """Sum of removed elements up to index i"""
            i += 1
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & (-i)
            return total

        result = []

        for pos in range(n):
            # Try each digit from smallest
            for digit in range(10):
                if not digit_positions[digit]:
                    continue

                # Original position of this digit
                orig_pos = digit_positions[digit][0]

                # Actual current position (accounting for previously moved elements)
                actual_pos = orig_pos - query(orig_pos)

                if actual_pos <= k:
                    # Can move this digit to current position
                    k -= actual_pos
                    result.append(str(digit))
                    digit_positions[digit].popleft()
                    update(orig_pos)
                    break

        return ''.join(result)


class SolutionSimple:
    def minInteger(self, num: str, k: int) -> str:
        """
        Simpler O(n^2) solution for smaller inputs.
        """
        num = list(num)
        n = len(num)

        for i in range(n):
            # Find smallest digit in range [i, min(i+k, n-1)]
            min_idx = i
            for j in range(i + 1, min(i + k + 1, n)):
                if num[j] < num[min_idx]:
                    min_idx = j

            # Bubble sort to bring num[min_idx] to position i
            swaps = min_idx - i
            k -= swaps

            # Perform the swaps
            while min_idx > i:
                num[min_idx], num[min_idx - 1] = num[min_idx - 1], num[min_idx]
                min_idx -= 1

        return ''.join(num)


class SolutionSegmentTree:
    def minInteger(self, num: str, k: int) -> str:
        """
        Using segment tree for range queries.
        """
        from collections import deque

        n = len(num)
        if k >= n * (n - 1) // 2:
            return ''.join(sorted(num))

        # Segment tree to count removed elements
        tree = [0] * (4 * n)

        def update(node: int, start: int, end: int, idx: int) -> None:
            if start == end:
                tree[node] = 1
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx)
            else:
                update(2 * node + 1, mid + 1, end, idx)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

        def query(node: int, start: int, end: int, l: int, r: int) -> int:
            if r < start or l > end:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return (query(2 * node, start, mid, l, r) +
                    query(2 * node + 1, mid + 1, end, l, r))

        digit_positions = [deque() for _ in range(10)]
        for i, ch in enumerate(num):
            digit_positions[int(ch)].append(i)

        result = []

        for _ in range(n):
            for digit in range(10):
                if not digit_positions[digit]:
                    continue

                orig_pos = digit_positions[digit][0]
                removed_before = query(1, 0, n - 1, 0, orig_pos - 1) if orig_pos > 0 else 0
                actual_pos = orig_pos - removed_before

                if actual_pos <= k:
                    k -= actual_pos
                    result.append(str(digit))
                    digit_positions[digit].popleft()
                    update(1, 0, n - 1, orig_pos)
                    break

        return ''.join(result)
