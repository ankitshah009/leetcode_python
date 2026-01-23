#858. Mirror Reflection
#Medium
#
#There is a special square room with mirrors on each of the four walls. Except
#for the southwest corner, there are receptors on each of the remaining corners,
#numbered 0, 1, and 2.
#
#The square room has walls of length p and a laser ray from the southwest corner
#first meets the east wall at a distance q from the 0th receptor.
#
#Given the two integers p and q, return the number of the receptor that the ray
#meets first.
#
#The test cases are guaranteed so that the ray will meet a receptor eventually.
#
#Example 1:
#Input: p = 2, q = 1
#Output: 2
#
#Example 2:
#Input: p = 3, q = 1
#Output: 1
#
#Constraints:
#    1 <= q <= p <= 1000

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        Simulate by unfolding the room.
        After traveling distance m*p vertically, ray hits:
        - Receptor 0 if m is even and on right wall
        - Receptor 1 if m is odd and on right wall
        - Receptor 2 if m is odd and on left wall

        Find smallest m where m*q is divisible by p.
        """
        from math import gcd

        g = gcd(p, q)
        p, q = p // g, q // g

        # After m bounces vertically, ray has traveled m*q in y direction
        # It reaches a corner when m*q is multiple of p
        # m = p/gcd(p,q), total height = p*q/gcd(p,q)

        # If p is odd and q is odd: receptor 1
        # If p is odd and q is even: receptor 0
        # If p is even and q is odd: receptor 2

        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1


class SolutionSimulation:
    """Simulation approach"""

    def mirrorReflection(self, p: int, q: int) -> int:
        from math import gcd

        # LCM gives the height at which ray hits corner
        lcm = p * q // gcd(p, q)

        # Number of reflections off horizontal walls
        m = lcm // q

        # Number of reflections off vertical walls
        n = lcm // p

        # Determine which corner
        if n % 2 == 0:
            return 2  # Left wall, top
        elif m % 2 == 0:
            return 0  # Right wall, bottom
        else:
            return 1  # Right wall, top


class SolutionMath:
    """Pure math solution"""

    def mirrorReflection(self, p: int, q: int) -> int:
        # Reduce to coprime
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2

        # Now at least one of p, q is odd
        if p % 2 == 0:
            return 2
        if q % 2 == 0:
            return 0
        return 1
