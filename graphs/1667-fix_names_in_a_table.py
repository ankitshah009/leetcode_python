#1667. Fix Names in a Table
#Easy
#
#SQL Schema problem - implementing logic in Python
#
#Table: Users
#+----------------+---------+
#| Column Name    | Type    |
#+----------------+---------+
#| user_id        | int     |
#| name           | varchar |
#+----------------+---------+
#user_id is the primary key.
#This table contains the ID and the name of the user. The name consists of only
#lowercase and uppercase characters.
#
#Write a query to fix the names so that only the first character is uppercase
#and the rest are lowercase.
#
#Return the result table ordered by user_id.

from typing import List, Dict

class Solution:
    def fixNames(self, users: List[Dict]) -> List[Dict]:
        """
        Capitalize the first letter and lowercase the rest.
        """
        results = []

        for user in users:
            fixed_name = user['name'].capitalize()
            results.append({
                'user_id': user['user_id'],
                'name': fixed_name
            })

        return sorted(results, key=lambda x: x['user_id'])


class SolutionManual:
    def fixNames(self, users: List[Dict]) -> List[Dict]:
        """
        Manual string manipulation.
        """
        results = []

        for user in users:
            name = user['name']
            if name:
                fixed = name[0].upper() + name[1:].lower()
            else:
                fixed = ''

            results.append({
                'user_id': user['user_id'],
                'name': fixed
            })

        return sorted(results, key=lambda x: x['user_id'])


class SolutionTitle:
    def fixNames(self, users: List[Dict]) -> List[Dict]:
        """
        Using title() for single-word names.
        Note: title() capitalizes first letter of each word.
        """
        return sorted(
            [{'user_id': u['user_id'], 'name': u['name'].capitalize()}
             for u in users],
            key=lambda x: x['user_id']
        )


class SolutionSQL:
    """
    SQL equivalent:

    SELECT
        user_id,
        CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
    FROM Users
    ORDER BY user_id;

    -- Or using INITCAP in some databases:
    -- SELECT user_id, INITCAP(name) AS name FROM Users ORDER BY user_id;
    """
    pass


class SolutionCompact:
    def fixNames(self, users: List[Dict]) -> List[Dict]:
        """
        One-liner solution.
        """
        return sorted(
            [{'user_id': u['user_id'], 'name': u['name'].capitalize()}
             for u in users],
            key=lambda x: x['user_id']
        )
