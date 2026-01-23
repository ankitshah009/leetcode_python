#1634. Add Two Polynomials Represented as Linked Lists
#Medium
#
#A polynomial linked list is a special type of linked list where every node
#represents a term in a polynomial expression.
#
#Each node has three attributes:
#- coefficient: an integer representing the number multiplier of the term.
#  The coefficient of the term 9x^4 is 9.
#- power: an integer representing the exponent. The power of the term 9x^4 is 4.
#- next: a pointer to the next node in the list, or null if it is the last node
#  of the list.
#
#For example, the polynomial 5x^3 + 4x - 7 is represented by the polynomial
#linked list: [[5,3],[4,1],[-7,0]].
#
#The polynomial linked list must be in its standard form: the polynomial must
#be in strictly descending order by its power value. Also, terms with a
#coefficient of 0 are omitted.
#
#Given two polynomial linked list heads, poly1 and poly2, add the polynomials
#together and return the head of the sum of the polynomials.
#
#PolyNode format: The input/output format is as a list of n nodes, where each
#node is represented as its [coefficient, power]. For example, the polynomial
#5x^3 + 4x - 7 would be represented as: [[5,3],[4,1],[-7,0]].
#
#Example 1:
#Input: poly1 = [[1,1]], poly2 = [[1,0]]
#Output: [[1,1],[1,0]]
#Explanation: poly1 = x, poly2 = 1. The sum is x + 1.
#
#Example 2:
#Input: poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]]
#Output: [[5,2],[2,0]]
#Explanation: poly1 = 2x^2 + 4x + 3, poly2 = 3x^2 - 4x - 1. The sum is 5x^2 + 2.
#
#Example 3:
#Input: poly1 = [[1,2]], poly2 = [[-1,2]]
#Output: []
#Explanation: The sum is 0, so we return an empty list.
#
#Constraints:
#    0 <= n <= 10^4
#    -10^9 <= PolyNode.coefficient <= 10^9
#    PolyNode.coefficient != 0
#    0 <= PolyNode.power <= 10^9
#    PolyNode.power > PolyNode.next.power

class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        """
        Merge two sorted lists, combining terms with same power.
        """
        dummy = PolyNode()
        current = dummy

        while poly1 and poly2:
            if poly1.power > poly2.power:
                current.next = PolyNode(poly1.coefficient, poly1.power)
                current = current.next
                poly1 = poly1.next
            elif poly2.power > poly1.power:
                current.next = PolyNode(poly2.coefficient, poly2.power)
                current = current.next
                poly2 = poly2.next
            else:
                # Same power, add coefficients
                coeff_sum = poly1.coefficient + poly2.coefficient
                if coeff_sum != 0:
                    current.next = PolyNode(coeff_sum, poly1.power)
                    current = current.next
                poly1 = poly1.next
                poly2 = poly2.next

        # Append remaining terms
        while poly1:
            current.next = PolyNode(poly1.coefficient, poly1.power)
            current = current.next
            poly1 = poly1.next

        while poly2:
            current.next = PolyNode(poly2.coefficient, poly2.power)
            current = current.next
            poly2 = poly2.next

        return dummy.next


class SolutionInPlace:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        """
        In-place modification (reuse existing nodes).
        """
        dummy = PolyNode()
        tail = dummy

        while poly1 and poly2:
            if poly1.power > poly2.power:
                tail.next = poly1
                poly1 = poly1.next
            elif poly2.power > poly1.power:
                tail.next = poly2
                poly2 = poly2.next
            else:
                coeff = poly1.coefficient + poly2.coefficient
                if coeff != 0:
                    poly1.coefficient = coeff
                    tail.next = poly1
                else:
                    # Skip this term (coefficient is 0)
                    tail = tail  # Don't advance tail
                    poly1 = poly1.next
                    poly2 = poly2.next
                    continue

                poly1 = poly1.next
                poly2 = poly2.next

            tail = tail.next

        tail.next = poly1 if poly1 else poly2

        return dummy.next


class SolutionDict:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        """
        Using dictionary to combine terms, then reconstruct.
        """
        terms = {}

        # Collect terms from poly1
        while poly1:
            terms[poly1.power] = terms.get(poly1.power, 0) + poly1.coefficient
            poly1 = poly1.next

        # Add terms from poly2
        while poly2:
            terms[poly2.power] = terms.get(poly2.power, 0) + poly2.coefficient
            poly2 = poly2.next

        # Build result in descending order of power
        dummy = PolyNode()
        current = dummy

        for power in sorted(terms.keys(), reverse=True):
            coeff = terms[power]
            if coeff != 0:
                current.next = PolyNode(coeff, power)
                current = current.next

        return dummy.next
