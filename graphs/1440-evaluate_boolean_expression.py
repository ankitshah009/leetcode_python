#1440. Evaluate Boolean Expression
#Medium
#
#Table: Variables
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| name          | varchar |
#| value         | int     |
#+---------------+---------+
#name is the primary key for this table.
#This table contains the stored variables and their values.
#
#Table: Expressions
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| left_operand  | varchar |
#| operator      | enum    |
#+---------------+---------+
#(left_operand, operator, right_operand) is the primary key for this table.
#This table contains a boolean expression that should be evaluated.
#operator is an enum that takes one of the values ('<', '>', '=')
#
#Write an SQL query to evaluate the boolean expressions in Expressions table.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Variables table:
#+------+-------+
#| name | value |
#+------+-------+
#| x    | 66    |
#| y    | 77    |
#+------+-------+
#Expressions table:
#+--------------+----------+---------------+
#| left_operand | operator | right_operand |
#+--------------+----------+---------------+
#| x            | >        | y             |
#| x            | <        | y             |
#| x            | =        | y             |
#| y            | >        | x             |
#| y            | <        | x             |
#| x            | =        | x             |
#+--------------+----------+---------------+
#Output:
#+--------------+----------+---------------+-------+
#| left_operand | operator | right_operand | value |
#+--------------+----------+---------------+-------+
#| x            | >        | y             | false |
#| x            | <        | y             | true  |
#| x            | =        | y             | false |
#| y            | >        | x             | true  |
#| y            | <        | x             | false |
#| x            | =        | x             | true  |
#+--------------+----------+---------------+-------+

#SQL Solution:
#SELECT
#    e.left_operand,
#    e.operator,
#    e.right_operand,
#    CASE
#        WHEN e.operator = '<' AND v1.value < v2.value THEN 'true'
#        WHEN e.operator = '>' AND v1.value > v2.value THEN 'true'
#        WHEN e.operator = '=' AND v1.value = v2.value THEN 'true'
#        ELSE 'false'
#    END AS value
#FROM Expressions e
#JOIN Variables v1 ON e.left_operand = v1.name
#JOIN Variables v2 ON e.right_operand = v2.name;

from typing import List
import operator

class Solution:
    def evaluateBooleanExpression(
        self, variables: List[dict], expressions: List[dict]
    ) -> List[dict]:
        """
        Python simulation of SQL query.
        Look up variable values and evaluate expressions.
        """
        # Build variable lookup
        var_values = {v['name']: v['value'] for v in variables}

        result = []
        for expr in expressions:
            left = var_values[expr['left_operand']]
            right = var_values[expr['right_operand']]
            op = expr['operator']

            if op == '<':
                value = 'true' if left < right else 'false'
            elif op == '>':
                value = 'true' if left > right else 'false'
            else:  # '='
                value = 'true' if left == right else 'false'

            result.append({
                'left_operand': expr['left_operand'],
                'operator': op,
                'right_operand': expr['right_operand'],
                'value': value
            })

        return result


class SolutionOperatorModule:
    def evaluateBooleanExpression(
        self, variables: List[dict], expressions: List[dict]
    ) -> List[dict]:
        """Using operator module for cleaner comparison"""
        var_values = {v['name']: v['value'] for v in variables}

        # Map operators to functions
        ops = {
            '<': operator.lt,
            '>': operator.gt,
            '=': operator.eq
        }

        result = []
        for expr in expressions:
            left = var_values[expr['left_operand']]
            right = var_values[expr['right_operand']]
            op_func = ops[expr['operator']]

            evaluated = op_func(left, right)

            result.append({
                'left_operand': expr['left_operand'],
                'operator': expr['operator'],
                'right_operand': expr['right_operand'],
                'value': 'true' if evaluated else 'false'
            })

        return result
