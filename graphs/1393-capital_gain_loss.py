#1393. Capital Gain/Loss
#Medium
#
#Table: Stocks
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| stock_name    | varchar |
#| operation     | enum    |
#| operation_day | int     |
#| price         | int     |
#+---------------+---------+
#(stock_name, operation_day) is the primary key for this table.
#operation column is an ENUM of type ('Sell', 'Buy')
#Each row of this table indicates that the stock which has stock_name had an
#operation on the day operation_day with the price.
#It is guaranteed that each 'Sell' operation for a stock has a corresponding
#'Buy' operation in a previous day. It is also guaranteed that each 'Buy'
#operation for a stock has a corresponding 'Sell' operation in an upcoming day.
#
#Write an SQL query to report the Capital gain/loss for each stock.
#The Capital gain/loss of a stock is the total gain or loss after buying and
#selling the stock one or many times.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Stocks table:
#+---------------+-----------+---------------+--------+
#| stock_name    | operation | operation_day | price  |
#+---------------+-----------+---------------+--------+
#| Leetcode      | Buy       | 1             | 1000   |
#| Corona Coverage | Buy     | 2             | 10     |
#| Leetcode      | Sell      | 5             | 9000   |
#| Haneli        | Buy       | 3             | 1000   |
#| Corona Coverage | Sell    | 4             | 1000   |
#| Corona Coverage | Buy     | 5             | 500    |
#| Corona Coverage | Sell    | 6             | 1000   |
#| Haneli        | Sell      | 6             | 1010   |
#| Leetcode      | Buy       | 8             | 7000   |
#| Leetcode      | Sell      | 10            | 10000  |
#+---------------+-----------+---------------+--------+
#Output:
#+---------------+---------------+
#| stock_name    | capital_gain_loss |
#+---------------+---------------+
#| Corona Coverage | 1490          |
#| Haneli        | 10            |
#| Leetcode      | 11000         |
#+---------------+---------------+

#SQL Solution:
#SELECT
#    stock_name,
#    SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) as capital_gain_loss
#FROM Stocks
#GROUP BY stock_name;

from typing import List
from collections import defaultdict

class Solution:
    def capitalGainLoss(self, stocks: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        For each stock, sum sells and subtract buys.
        """
        gains = defaultdict(int)

        for record in stocks:
            stock = record['stock_name']
            operation = record['operation']
            price = record['price']

            if operation == 'Sell':
                gains[stock] += price
            else:  # Buy
                gains[stock] -= price

        return [{'stock_name': stock, 'capital_gain_loss': gain}
                for stock, gain in gains.items()]


class SolutionExplicit:
    def capitalGainLoss(self, stocks: List[dict]) -> List[dict]:
        """More explicit tracking of buys and sells"""
        buys = defaultdict(int)
        sells = defaultdict(int)

        for record in stocks:
            stock = record['stock_name']
            operation = record['operation']
            price = record['price']

            if operation == 'Buy':
                buys[stock] += price
            else:
                sells[stock] += price

        all_stocks = set(buys.keys()) | set(sells.keys())

        return [{'stock_name': stock,
                 'capital_gain_loss': sells[stock] - buys[stock]}
                for stock in all_stocks]
