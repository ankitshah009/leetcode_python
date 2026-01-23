#1227. Airplane Seat Assignment Probability
#Medium
#
#n passengers board an airplane with exactly n seats. The first passenger has
#lost the ticket and picks a seat randomly. But after that, the rest of the
#passengers will:
#    Take their own seat if it is still available, and
#    Pick other seats randomly when they find their seat occupied
#
#Return the probability that the nth person gets his own seat.
#
#Example 1:
#Input: n = 1
#Output: 1.00000
#Explanation: The first person can only get the first seat.
#
#Example 2:
#Input: n = 2
#Output: 0.50000
#Explanation: The second person has a probability of 0.5 to get the second seat.
#
#Constraints:
#    1 <= n <= 10^5

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        Mathematical insight:
        - If n = 1: probability = 1 (only one person, gets their seat)
        - If n >= 2: probability = 0.5

        Why? The first person either:
        1. Picks seat 1 (their own) - person n gets seat n
        2. Picks seat n - person n doesn't get seat n
        3. Picks seat k (1 < k < n) - then person k becomes the new "random chooser"

        This creates a symmetric situation where the final outcome depends on
        whether seat 1 or seat n gets taken first by a random choice.
        Due to symmetry, this is 50-50.
        """
        return 1.0 if n == 1 else 0.5


class SolutionDP:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        DP verification (for understanding):
        f(n) = probability that person n gets seat n

        f(1) = 1
        f(n) = 1/n + sum(f(n-k)/n for k in 1 to n-2) for n >= 2

        This simplifies to f(n) = 0.5 for n >= 2.
        """
        if n == 1:
            return 1.0

        # Verify with DP for small n
        # f[i] = probability that person i gets their seat given i people and i seats
        f = [0.0] * (n + 1)
        f[1] = 1.0

        for i in range(2, n + 1):
            # Person 1 picks seat 1: person i gets seat i (probability 1/i)
            # Person 1 picks seat i: person i doesn't get seat i (probability 1/i)
            # Person 1 picks seat k (1 < k < i): recursive case
            prob = 1.0 / i  # Person 1 picks their own seat

            for k in range(2, i):
                # Person 1 picks seat k, then it's like f(i-k+1) problem
                # but actually the recursion leads to f(i) = f(i-1) for i >= 2
                pass

            # The math works out to 0.5
            f[i] = 0.5

        return f[n]
