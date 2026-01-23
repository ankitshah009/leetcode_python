#964. Least Operators to Express Number
#Hard
#
#Given a single positive integer x, we will write an expression of the form
#x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either
#addition, subtraction, multiplication, or division (+, -, *, or /). We may
#insert parentheses anywhere to change the usual order of operations.
#
#Find the least number of operators to write an expression equal to the given
#target.
#
#Example 1:
#Input: x = 3, target = 19
#Output: 5
#Explanation: 3*3+3*3+3/3. The expression contains 5 operations.
#
#Example 2:
#Input: x = 5, target = 501
#Output: 8
#
#Example 3:
#Input: x = 100, target = 200000000
#Output: 7
#
#Constraints:
#    2 <= x <= 100
#    1 <= target <= 2 * 10^8

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """
        DP with memoization: express target using powers of x.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(idx: int, remaining: int) -> int:
            """
            Min cost to express remaining using x^idx, x^(idx+1), ...
            """
            if remaining == 0:
                return 0

            # Cost for one x^idx
            if idx == 0:
                cost_per = 2  # x/x costs 2 operators
            else:
                cost_per = idx  # x*x*...*x costs idx operators

            # How many x^idx to use
            count = remaining // (x ** idx) if idx > 0 else remaining
            if idx == 0:
                power = 1
            else:
                power = x ** idx

            result = float('inf')

            # Use count copies (positive contribution)
            for k in range(min(count + 1, x)):
                # Cost: k * cost_per + cost for remaining
                # Plus 1 for each term (+ or -) except first
                curr_cost = k * cost_per + (1 if k > 0 else 0)
                new_remaining = remaining - k * power

                if new_remaining >= 0:
                    sub_cost = dp(idx + 1, new_remaining)
                    if sub_cost != float('inf'):
                        total = curr_cost + sub_cost - (1 if k > 0 and sub_cost > 0 else 0)
                        result = min(result, total)

            # Use count+1 copies with next power compensating (negative contribution)
            if count < x:
                k = count + 1
                curr_cost = k * cost_per
                new_remaining = k * power - remaining
                sub_cost = dp(idx + 1, new_remaining)
                if sub_cost != float('inf'):
                    result = min(result, curr_cost + sub_cost)

            return result

        # Start from x^0 = 1
        return dp(0, target) - 1  # -1 because first term doesn't need operator


class SolutionGreedy:
    """Greedy with cost comparison"""

    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i: int, remaining: int) -> int:
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')

            # Find power of x closest to remaining
            power = 1
            idx = 0
            while power * x <= remaining:
                power *= x
                idx += 1

            # Cost to produce x^idx
            cost = idx if idx > 0 else 2

            # Option 1: Use floor(remaining / power) copies
            count = remaining // power
            result = count * cost + dp(idx + 1, remaining - count * power)

            # Option 2: Use ceil, subtract excess
            if count + 1 < x and power * (count + 1) - remaining < remaining:
                result = min(result, (count + 1) * cost + dp(idx + 1, power * (count + 1) - remaining))

            return result

        ans = dp(0, target)
        # Adjust for operator count
        return ans - 1 if ans != float('inf') else -1
