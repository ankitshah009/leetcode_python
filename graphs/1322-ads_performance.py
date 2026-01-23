#1322. Ads Performance
#Easy
#
#Table: Ads
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| ad_id         | int     |
#| user_id       | int     |
#| action        | enum    |
#+---------------+---------+
#(ad_id, user_id) is the primary key for this table.
#Each row of this table contains the ID of an Ad, the ID of a user, and the
#action taken by this user regarding this Ad.
#The action column is an ENUM type of ('Clicked', 'Viewed', 'Ignored').
#
#A company is running Ads and wants to calculate the performance of each Ad.
#
#Performance of the Ad is measured using Click-Through Rate (CTR) where:
#CTR = (Clicked / (Clicked + Viewed)) * 100
#
#Write an SQL query to find the ctr of each Ad. Round ctr to two decimal points.
#
#Return the result table ordered by ctr in descending order and by ad_id in
#ascending order in case of a tie.
#
#Example 1:
#Input:
#Ads table:
#+-------+---------+---------+
#| ad_id | user_id | action  |
#+-------+---------+---------+
#| 1     | 1       | Clicked |
#| 2     | 2       | Clicked |
#| 3     | 3       | Viewed  |
#| 5     | 5       | Ignored |
#| 1     | 7       | Ignored |
#| 2     | 7       | Viewed  |
#| 3     | 5       | Clicked |
#| 1     | 4       | Viewed  |
#| 2     | 11      | Viewed  |
#| 1     | 2       | Clicked |
#+-------+---------+---------+
#Output:
#+-------+-------+
#| ad_id | ctr   |
#+-------+-------+
#| 1     | 66.67 |
#| 3     | 50.00 |
#| 2     | 33.33 |
#| 5     | 0.00  |
#+-------+-------+

# SQL Solution:
# SELECT
#     ad_id,
#     ROUND(
#         IFNULL(
#             100.0 * SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) /
#             NULLIF(SUM(CASE WHEN action IN ('Clicked', 'Viewed') THEN 1 ELSE 0 END), 0),
#             0
#         ),
#         2
#     ) AS ctr
# FROM Ads
# GROUP BY ad_id
# ORDER BY ctr DESC, ad_id ASC;

# Python simulation
from typing import List, Tuple
from collections import defaultdict

class Solution:
    def adsPerformance(
        self,
        ads: List[Tuple[int, int, str]]
    ) -> List[Tuple[int, float]]:
        """
        Calculate CTR for each ad.
        CTR = Clicked / (Clicked + Viewed) * 100
        """
        # Count clicks and views per ad
        clicks = defaultdict(int)
        views = defaultdict(int)
        all_ads = set()

        for ad_id, user_id, action in ads:
            all_ads.add(ad_id)
            if action == 'Clicked':
                clicks[ad_id] += 1
            elif action == 'Viewed':
                views[ad_id] += 1

        result = []
        for ad_id in all_ads:
            total = clicks[ad_id] + views[ad_id]
            if total == 0:
                ctr = 0.0
            else:
                ctr = round(100.0 * clicks[ad_id] / total, 2)
            result.append((ad_id, ctr))

        # Sort by ctr desc, then ad_id asc
        result.sort(key=lambda x: (-x[1], x[0]))

        return result
