#1357. Apply Discount Every n Orders
#Medium
#
#There is a supermarket that is frequented by many customers. The products sold
#at the supermarket are represented as two parallel integer arrays products and
#prices, where the ith product has an ID of products[i] and a price of prices[i].
#
#When a customer is paying, their bill is represented as two parallel integer
#arrays product and amount, where the jth product they purchased has an ID of
#product[j], and amount[j] is how much of the product they bought. Their
#subtotal is calculated as the sum of each amount[j] * (price of the jth product).
#
#The supermarket decides to have a sale. Every nth customer paying for their
#groceries will be given a percentage discount. The discount amount is given by
#discount, where they will be given discount percent off their subtotal. More
#formally, if their subtotal is bill, then they would actually pay
#bill * ((100 - discount) / 100).
#
#Implement the Cashier class:
#    Cashier(int n, int discount, int[] products, int[] prices) Initializes the
#    object with n, the discount, and the products and their prices.
#    double getBill(int[] product, int[] amount) Returns the final total of the
#    bill with the discount applied (if any).
#
#Constraints:
#    1 <= n <= 10^4
#    0 <= discount <= 100
#    1 <= products.length <= 200
#    prices.length == products.length
#    1 <= products[i] <= 200
#    1 <= prices[i] <= 1000
#    The elements in products are unique.
#    1 <= product.length <= products.length
#    amount.length == product.length
#    product[j] exists in products.
#    1 <= amount[j] <= 1000
#    The elements of product are unique.
#    At most 1000 calls will be made to getBill.
#    Answers within 10^-5 of the actual value will be accepted.

from typing import List

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.price_map = {p: pr for p, pr in zip(products, prices)}
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1

        # Calculate subtotal
        subtotal = sum(self.price_map[p] * a for p, a in zip(product, amount))

        # Apply discount if nth customer
        if self.customer_count % self.n == 0:
            return subtotal * (100 - self.discount) / 100

        return float(subtotal)


class CashierAlt:
    """Alternative implementation"""

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount_multiplier = (100 - discount) / 100
        self.price_map = dict(zip(products, prices))
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1

        bill = sum(self.price_map[p] * a for p, a in zip(product, amount))

        if self.count == self.n:
            self.count = 0  # Reset counter
            return bill * self.discount_multiplier

        return float(bill)
