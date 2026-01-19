#248. Strobogrammatic Number III
#Hard
#
#Given two strings low and high that represent two integers low and high where
#low <= high, return the number of strobogrammatic numbers in the range [low, high].
#
#A strobogrammatic number is a number that looks the same when rotated 180 degrees
#(looked at upside down).
#
#Example 1:
#Input: low = "50", high = "100"
#Output: 3
#
#Example 2:
#Input: low = "0", high = "0"
#Output: 1
#
#Constraints:
#    1 <= low.length, high.length <= 15
#    low and high consist of only digits.
#    low <= high
#    low and high do not contain any leading zeros except for zero itself.

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """Generate all strobogrammatic numbers and count those in range"""
        self.count = 0
        self.low = low
        self.high = high

        for length in range(len(low), len(high) + 1):
            self.dfs(length, "")

        return self.count

    def dfs(self, length, current):
        if len(current) > length:
            return

        if len(current) == length:
            # Check if in range
            if self.in_range(current):
                self.count += 1
            return

        remaining = length - len(current)

        if remaining == 1:
            # Middle character (odd length)
            for mid in ['0', '1', '8']:
                self.dfs(length, current[:len(current)//2] + mid + current[len(current)//2:])
        else:
            # Add pairs
            pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
            for left, right in pairs:
                # Skip leading zeros (except for "0" itself)
                if len(current) == 0 and left == '0' and length > 1:
                    continue
                self.dfs(length, left + current + right)

    def in_range(self, num):
        if len(num) < len(self.low) or len(num) > len(self.high):
            return False
        if len(num) == len(self.low) and num < self.low:
            return False
        if len(num) == len(self.high) and num > self.high:
            return False
        return True


class SolutionGenerate:
    """Generate all strobogrammatic numbers of each length"""

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def generate(n, is_outer):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']

            middles = generate(n - 2, False)
            result = []

            pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]

            for middle in middles:
                for left, right in pairs:
                    # Skip leading zeros for outer (non-recursive) calls
                    if is_outer and left == '0':
                        continue
                    result.append(left + middle + right)

            return result

        count = 0

        for length in range(len(low), len(high) + 1):
            nums = generate(length, length > 1)

            for num in nums:
                # Compare as strings (works because same length)
                if len(num) == len(low) and num < low:
                    continue
                if len(num) == len(high) and num > high:
                    continue
                count += 1

        return count


class SolutionIterative:
    """Iterative generation"""

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        single = ['0', '1', '8']

        def generate(n):
            if n == 0:
                return ['']
            if n == 1:
                return single[:]

            # Start from center and build outward
            if n % 2 == 0:
                current = ['']
            else:
                current = single[:]

            for _ in range((n - len(current[0])) // 2):
                next_level = []
                for num in current:
                    for left, right in pairs:
                        next_level.append(left + num + right)
                current = next_level

            # Remove leading zeros
            return [num for num in current if len(num) == 1 or num[0] != '0']

        count = 0
        for length in range(len(low), len(high) + 1):
            for num in generate(length):
                if len(num) == len(low) and num < low:
                    continue
                if len(num) == len(high) and num > high:
                    continue
                count += 1

        return count
