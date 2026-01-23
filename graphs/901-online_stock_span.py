#901. Online Stock Span
#Medium
#
#Design an algorithm that collects daily price quotes for some stock and returns
#the span of that stock's price for the current day.
#
#The span of the stock's price in one day is the maximum number of consecutive
#days (starting from that day and going backward) for which the stock price was
#less than or equal to the price of that day.
#
#Example 1:
#Input: ["StockSpanner","next","next","next","next","next","next","next"]
#       [[],[100],[80],[60],[70],[60],[75],[85]]
#Output: [null,1,1,1,2,1,4,6]
#
#Constraints:
#    1 <= price <= 10^5
#    At most 10^4 calls will be made to next.

class StockSpanner:
    """
    Monotonic stack storing (price, span) pairs.
    """

    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price: int) -> int:
        span = 1

        # Pop all prices less than or equal to current
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span


class StockSpannerIndex:
    """Store indices and prices"""

    def __init__(self):
        self.stack = []  # (index, price)
        self.day = -1

    def next(self, price: int) -> int:
        self.day += 1

        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()

        span = self.day - self.stack[-1][0] if self.stack else self.day + 1
        self.stack.append((self.day, price))
        return span


class StockSpannerBrute:
    """Brute force O(n) per call"""

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2

        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1

        return span
