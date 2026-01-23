#1517. Find Users With Valid E-Mails
#Easy (SQL)
#
#Table: Users
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| user_id       | int     |
#| name          | varchar |
#| mail          | varchar |
#+---------------+---------+
#user_id is the primary key for this table.
#This table contains information of the users signed up in a website. Some
#e-mails are invalid.
#
#Write an SQL query to find the users who have valid emails.
#
#A valid e-mail has a prefix name and a domain where:
#    The prefix name is a string that may contain letters (upper or lower case),
#    digits, underscore '_', period '.', and/or dash '-'. The prefix name must
#    start with a letter.
#    The domain is '@leetcode.com'.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Users table:
#+---------+-----------+-------------------------+
#| user_id | name      | mail                    |
#+---------+-----------+-------------------------+
#| 1       | Winston   | winston@leetcode.com    |
#| 2       | Jonathan  | jonathanisgreat         |
#| 3       | Annabelle | bella-@leetcode.com     |
#| 4       | Sally     | sally.come@leetcode.com |
#| 5       | Marwan    | quarz#2020@leetcode.com |
#| 6       | David     | david69@gmail.com       |
#| 7       | Shapiro   | .teleport@leetcode.com  |
#+---------+-----------+-------------------------+
#Output:
#+---------+-----------+-------------------------+
#| user_id | name      | mail                    |
#+---------+-----------+-------------------------+
#| 1       | Winston   | winston@leetcode.com    |
#| 3       | Annabelle | bella-@leetcode.com     |
#| 4       | Sally     | sally.come@leetcode.com |
#+---------+-----------+-------------------------+

#SQL Solution (MySQL):
#SELECT *
#FROM Users
#WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$';
#
#-- Alternative without REGEXP:
#-- SELECT *
#-- FROM Users
#-- WHERE mail LIKE '%@leetcode.com'
#--   AND mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$';

from typing import List
import re

class Solution:
    def findUsersWithValidEmails(self, users: List[dict]) -> List[dict]:
        """
        Python simulation using regex.
        Validate email format: starts with letter, contains valid chars, ends with @leetcode.com
        """
        # Regex pattern for valid email
        pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'

        result = []
        for user in users:
            if re.match(pattern, user['mail']):
                result.append(user)

        return result


class SolutionManual:
    def findUsersWithValidEmails(self, users: List[dict]) -> List[dict]:
        """
        Manual validation without regex.
        """
        def is_valid_email(email: str) -> bool:
            # Must end with @leetcode.com
            suffix = '@leetcode.com'
            if not email.endswith(suffix):
                return False

            # Get prefix (part before @leetcode.com)
            prefix = email[:-len(suffix)]

            if not prefix:
                return False

            # Must start with a letter
            if not prefix[0].isalpha():
                return False

            # Rest can be letters, digits, underscore, period, dash
            valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-')

            for char in prefix:
                if char not in valid_chars:
                    return False

            return True

        return [user for user in users if is_valid_email(user['mail'])]


class SolutionCompiled:
    def __init__(self):
        # Pre-compile regex for efficiency
        self.pattern = re.compile(r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$')

    def findUsersWithValidEmails(self, users: List[dict]) -> List[dict]:
        """Using pre-compiled regex"""
        return [user for user in users if self.pattern.match(user['mail'])]


class SolutionExplicit:
    def findUsersWithValidEmails(self, users: List[dict]) -> List[dict]:
        """
        Explicit validation with detailed checks.
        """
        def validate(email: str) -> bool:
            # Split by @
            parts = email.split('@')

            # Must have exactly one @
            if len(parts) != 2:
                return False

            prefix, domain = parts

            # Domain must be exactly leetcode.com
            if domain != 'leetcode.com':
                return False

            # Prefix must be non-empty
            if not prefix:
                return False

            # First character must be a letter
            if not prefix[0].isalpha():
                return False

            # All characters must be valid
            allowed = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-')
            return all(c in allowed for c in prefix)

        return [user for user in users if validate(user['mail'])]
