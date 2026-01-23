#1801. Number of Orders in the Backlog
#Medium
#
#You are given a 2D integer array orders, where each orders[i] = [price_i,
#amount_i, orderType_i] denotes that amount_i orders have been placed of type
#orderType_i at the price price_i:
#- If orderType_i == 0, then it is a batch of buy orders.
#- If orderType_i == 1, then it is a batch of sell orders.
#
#Return the total amount of orders in the backlog after placing all the orders
#from the input. Since this number can be large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: orders = [[10,5,0],[15,2,1],[25,1,0],[30,4,0]]
#Output: 6
#
#Example 2:
#Input: orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
#Output: 999999984
#
#Constraints:
#    1 <= orders.length <= 10^5
#    orders[i].length == 3
#    1 <= price_i, amount_i <= 10^9
#    orderType_i is either 0 or 1.

from typing import List
import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        """
        Use two heaps: max-heap for buy orders, min-heap for sell orders.
        """
        MOD = 10**9 + 7
        buy_heap = []   # max-heap (negated prices)
        sell_heap = []  # min-heap

        for price, amount, order_type in orders:
            if order_type == 0:  # Buy order
                # Match with sell orders
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_heap)
                    matched = min(amount, sell_amount)
                    amount -= matched
                    sell_amount -= matched
                    if sell_amount > 0:
                        heapq.heappush(sell_heap, (sell_price, sell_amount))

                if amount > 0:
                    heapq.heappush(buy_heap, (-price, amount))

            else:  # Sell order
                # Match with buy orders
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_heap)
                    matched = min(amount, buy_amount)
                    amount -= matched
                    buy_amount -= matched
                    if buy_amount > 0:
                        heapq.heappush(buy_heap, (buy_price, buy_amount))

                if amount > 0:
                    heapq.heappush(sell_heap, (price, amount))

        # Sum remaining orders
        total = sum(amt for _, amt in buy_heap) + sum(amt for _, amt in sell_heap)
        return total % MOD
