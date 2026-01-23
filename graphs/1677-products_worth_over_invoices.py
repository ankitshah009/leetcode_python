#1677. Product's Worth Over Invoices
#Easy
#
#SQL Schema problem - implementing logic in Python
#
#Table: Product
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| product_id  | int     |
#| name        | varchar |
#+-------------+---------+
#product_id is the primary key.
#
#Table: Invoice
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| invoice_id  | int  |
#| product_id  | int  |
#| rest        | int  |
#| paid        | int  |
#| canceled    | int  |
#| refunded    | int  |
#+-------------+------+
#invoice_id is the primary key.
#
#Write a query that returns the product_id, name and the total rest, paid,
#canceled, and refunded for each product.

from typing import List, Dict
from collections import defaultdict

class Solution:
    def productsWorth(self, products: List[Dict],
                      invoices: List[Dict]) -> List[Dict]:
        """
        Aggregate invoice amounts by product.
        """
        # Create product name lookup
        product_names = {p['product_id']: p['name'] for p in products}

        # Aggregate invoices by product
        aggregates = defaultdict(lambda: {'rest': 0, 'paid': 0, 'canceled': 0, 'refunded': 0})

        for inv in invoices:
            pid = inv['product_id']
            aggregates[pid]['rest'] += inv['rest']
            aggregates[pid]['paid'] += inv['paid']
            aggregates[pid]['canceled'] += inv['canceled']
            aggregates[pid]['refunded'] += inv['refunded']

        # Build result
        results = []
        for pid in product_names:
            agg = aggregates[pid]
            results.append({
                'product_id': pid,
                'name': product_names[pid],
                'rest': agg['rest'],
                'paid': agg['paid'],
                'canceled': agg['canceled'],
                'refunded': agg['refunded']
            })

        return sorted(results, key=lambda x: x['product_id'])


class SolutionSQL:
    """
    SQL equivalent:

    SELECT
        p.product_id,
        p.name,
        COALESCE(SUM(i.rest), 0) AS rest,
        COALESCE(SUM(i.paid), 0) AS paid,
        COALESCE(SUM(i.canceled), 0) AS canceled,
        COALESCE(SUM(i.refunded), 0) AS refunded
    FROM Product p
    LEFT JOIN Invoice i ON p.product_id = i.product_id
    GROUP BY p.product_id, p.name
    ORDER BY p.product_id;
    """
    pass


class SolutionCompact:
    def productsWorth(self, products: List[Dict],
                      invoices: List[Dict]) -> List[Dict]:
        """
        Compact implementation.
        """
        names = {p['product_id']: p['name'] for p in products}
        sums = defaultdict(lambda: [0, 0, 0, 0])  # rest, paid, canceled, refunded

        for inv in invoices:
            pid = inv['product_id']
            sums[pid][0] += inv['rest']
            sums[pid][1] += inv['paid']
            sums[pid][2] += inv['canceled']
            sums[pid][3] += inv['refunded']

        return sorted([
            {
                'product_id': pid,
                'name': names[pid],
                'rest': sums[pid][0],
                'paid': sums[pid][1],
                'canceled': sums[pid][2],
                'refunded': sums[pid][3]
            }
            for pid in names
        ], key=lambda x: x['product_id'])
