#1096. Brace Expansion II
#Hard
#
#Under the grammar given below, strings can represent a set of lowercase words.
#Let R(expr) denote the set of words the expression represents.
#
#The grammar can best be understood through simple examples:
#    Single letters just represent a singleton set containing that word.
#        R("a") = {"a"}
#        R("w") = {"w"}
#    When we take a comma-delimited list of two or more expressions, we take
#    the union of possibilities.
#        R("{a,b,c}") = {"a","b","c"}
#        R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only
#        contains each word at most once)
#    When we concatenate two expressions, we take the set of possible
#    concatenations between two words where the first word comes from the
#    first expression and the second word comes from the second expression.
#        R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
#        R("a{b,c}{d,e}f{g,h}") = {"abdfg","abdfh","abefg","abefh","acdfg",
#        "acdfh","acefg","acefh"}
#
#Formally, the three rules for our grammar:
#    For every lowercase letter x, we have R(x) = {x}.
#    For expressions e1, e2, ... , ek with k >= 2, we have
#    R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
#    For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b)
#    in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the
#    cartesian product.
#
#Given an expression representing a set of words under the given grammar,
#return the sorted list of words that the expression represents.
#
#Example 1:
#Input: expression = "{a,b}{c,{d,e}}"
#Output: ["ac","ad","ae","bc","bd","be"]
#
#Example 2:
#Input: expression = "{{a,z},a{b,c},{ab,z}}"
#Output: ["a","ab","ac","z"]
#
#Constraints:
#    1 <= expression.length <= 60
#    expression[i] consists of '{', '}', ','or lowercase English letters.
#    The given expression represents a set of words based on the grammar
#    given in the description.

from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        """
        Recursive descent parser.
        """
        def parse(expr, start):
            """Parse and return (set of strings, end index)"""
            groups = [set([''])]  # Start with empty string for concatenation
            i = start

            while i < len(expr):
                if expr[i] == '{':
                    # Find matching close brace and parse inside
                    inner_set, i = parse(expr, i + 1)
                    # Concatenate with current group
                    groups[-1] = {a + b for a in groups[-1] for b in inner_set}
                elif expr[i] == '}':
                    # End of current group
                    result = set()
                    for g in groups:
                        result |= g
                    return result, i + 1
                elif expr[i] == ',':
                    # Start new group (union)
                    groups.append(set(['']))
                    i += 1
                else:
                    # Letter - concatenate to current group
                    groups[-1] = {s + expr[i] for s in groups[-1]}
                    i += 1

            result = set()
            for g in groups:
                result |= g
            return result, i

        result_set, _ = parse(expression, 0)
        return sorted(result_set)


class SolutionStack:
    def braceExpansionII(self, expression: str) -> List[str]:
        """Stack-based parsing"""
        stack = []
        current_union = []
        current_product = {''}

        i = 0
        while i < len(expression):
            c = expression[i]

            if c == '{':
                # Save current state
                stack.append((current_union, current_product))
                current_union = []
                current_product = {''}
            elif c == '}':
                # Complete current group
                current_union.append(current_product)
                result = set()
                for s in current_union:
                    result |= s

                # Pop and concatenate
                prev_union, prev_product = stack.pop()
                current_product = {a + b for a in prev_product for b in result}
                current_union = prev_union
            elif c == ',':
                current_union.append(current_product)
                current_product = {''}
            else:
                current_product = {s + c for s in current_product}

            i += 1

        current_union.append(current_product)
        result = set()
        for s in current_union:
            result |= s

        return sorted(result)
