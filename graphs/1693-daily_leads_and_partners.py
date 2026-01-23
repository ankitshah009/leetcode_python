#1693. Daily Leads and Partners
#Easy
#
#SQL Schema problem - implementing logic in Python
#
#Table: DailySales
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| date_id     | date    |
#| make_name   | varchar |
#| lead_id     | int     |
#| partner_id  | int     |
#+-------------+---------+
#This table does not have a primary key. It may contain duplicates.
#
#Write a query that returns, for each date_id and make_name, the number of
#distinct lead_id's and the number of distinct partner_id's.

from typing import List, Dict
from collections import defaultdict

class Solution:
    def dailyLeadsAndPartners(self, sales: List[Dict]) -> List[Dict]:
        """
        Group by date_id and make_name, count distinct leads and partners.
        """
        groups = defaultdict(lambda: {'leads': set(), 'partners': set()})

        for sale in sales:
            key = (sale['date_id'], sale['make_name'])
            groups[key]['leads'].add(sale['lead_id'])
            groups[key]['partners'].add(sale['partner_id'])

        results = []
        for (date_id, make_name), data in sorted(groups.items()):
            results.append({
                'date_id': date_id,
                'make_name': make_name,
                'unique_leads': len(data['leads']),
                'unique_partners': len(data['partners'])
            })

        return results


class SolutionSQL:
    """
    SQL equivalent:

    SELECT
        date_id,
        make_name,
        COUNT(DISTINCT lead_id) AS unique_leads,
        COUNT(DISTINCT partner_id) AS unique_partners
    FROM DailySales
    GROUP BY date_id, make_name;
    """
    pass


class SolutionPandas:
    def dailyLeadsAndPartners(self, sales: List[Dict]) -> List[Dict]:
        """
        Pandas-style approach.
        """
        # Group and count unique
        grouped = defaultdict(lambda: {'leads': set(), 'partners': set()})

        for row in sales:
            key = (row['date_id'], row['make_name'])
            grouped[key]['leads'].add(row['lead_id'])
            grouped[key]['partners'].add(row['partner_id'])

        return sorted([
            {
                'date_id': k[0],
                'make_name': k[1],
                'unique_leads': len(v['leads']),
                'unique_partners': len(v['partners'])
            }
            for k, v in grouped.items()
        ], key=lambda x: (x['date_id'], x['make_name']))


class SolutionCompact:
    def dailyLeadsAndPartners(self, sales: List[Dict]) -> List[Dict]:
        """
        Compact implementation.
        """
        from collections import defaultdict

        g = defaultdict(lambda: [set(), set()])

        for s in sales:
            k = (s['date_id'], s['make_name'])
            g[k][0].add(s['lead_id'])
            g[k][1].add(s['partner_id'])

        return sorted([
            {'date_id': d, 'make_name': m, 'unique_leads': len(l), 'unique_partners': len(p)}
            for (d, m), (l, p) in g.items()
        ], key=lambda x: (x['date_id'], x['make_name']))
