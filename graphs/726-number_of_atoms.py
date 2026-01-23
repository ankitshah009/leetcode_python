#726. Number of Atoms
#Hard
#
#Given a string formula representing a chemical formula, return the count of
#each atom.
#
#The atomic element always starts with an uppercase character, then zero or
#more lowercase letters, representing the name.
#
#One or more digits representing that element's count may follow if the count
#is greater than 1. If the count is 1, no digits will follow.
#- For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
#
#Two formulas can be concatenated together to produce another formula.
#- For example, "H2O2He3Mg4" is also a formula.
#
#A formula placed in parentheses, and a count (optionally added) is also a
#formula.
#- For example, "(H2O2)" and "(H2O2)3" are formulas.
#
#Return the count of all elements as a string in the following form: the first
#name (in sorted order), followed by its count (if that count is more than 1),
#followed by the second name (in sorted order), followed by its count, and so on.
#
#Example 1:
#Input: formula = "H2O"
#Output: "H2O"
#
#Example 2:
#Input: formula = "Mg(OH)2"
#Output: "H2MgO2"
#
#Example 3:
#Input: formula = "K4(ON(SO3)2)2"
#Output: "K4N2O14S4"
#
#Constraints:
#    1 <= formula.length <= 1000
#    formula consists of English letters, digits, '(', and ')'.
#    formula is always valid.

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Use stack to handle nested parentheses.
        """
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                # Parse multiplier
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i]) if start < i else 1

                # Pop and merge with parent
                top = stack.pop()
                for element, count in top.items():
                    stack[-1][element] += count * multiplier
            else:
                # Parse element name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]

                # Parse count
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if start < i else 1

                stack[-1][element] += count

        # Build result
        result = stack[0]
        return ''.join(
            element + (str(count) if count > 1 else '')
            for element, count in sorted(result.items())
        )


class SolutionRecursive:
    """Recursive descent parser"""

    def countOfAtoms(self, formula: str) -> str:
        self.i = 0
        self.formula = formula
        self.n = len(formula)

        def parse():
            counts = defaultdict(int)

            while self.i < self.n and self.formula[self.i] != ')':
                if self.formula[self.i] == '(':
                    self.i += 1  # Skip '('
                    inner = parse()
                    self.i += 1  # Skip ')'

                    # Get multiplier
                    mult = parse_number()
                    for elem, cnt in inner.items():
                        counts[elem] += cnt * mult
                else:
                    elem = parse_element()
                    cnt = parse_number()
                    counts[elem] += cnt

            return counts

        def parse_element():
            start = self.i
            self.i += 1
            while self.i < self.n and self.formula[self.i].islower():
                self.i += 1
            return self.formula[start:self.i]

        def parse_number():
            start = self.i
            while self.i < self.n and self.formula[self.i].isdigit():
                self.i += 1
            return int(self.formula[start:self.i]) if start < self.i else 1

        result = parse()
        return ''.join(
            elem + (str(cnt) if cnt > 1 else '')
            for elem, cnt in sorted(result.items())
        )
