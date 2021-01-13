#420. Strong Password Checker
#Hard
#
#A password is considered strong if the below conditions are all met:
#
#    It has at least 6 characters and at most 20 characters.
#    It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
#    It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
#
#Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.
#
#In one step, you can:
#
#    Insert one character to password,
#    Delete one character from password, or
#    Replace one character of password with another character.
#
# 
#
#Example 1:
#
#Input: password = "a"
#Output: 5
#
#Example 2:
#
#Input: password = "aA1"
#Output: 3
#
#Example 3:
#
#Input: password = "1337C0d3"
#Output: 0
#
# 
#
#Constraints:
#
#    1 <= password.length <= 50
#    password consists of letters, digits, dot '.' or exclamation mark '!'.
#

import itertools

class Solution:
    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    uppercase = set('ABCDEFGHIJKLMNOPQRSTUFVWXYZ')
    digit = set('0123456789')
    
    def strongPasswordChecker(self, s: str) -> int:
        characters = set(s)
        
        # Check rule (2)
        needs_lowercase = not (characters & self.lowercase)
        needs_uppercase = not (characters & self.uppercase)
        needs_digit = not (characters & self.digit)
        num_required_type_replaces = int(needs_lowercase + needs_uppercase + needs_digit)
        
        # Check rule (1)
        num_required_inserts = max(0, 6 - len(s))
        num_required_deletes = max(0, len(s) - 20)
        
        # Check rule (3)
        # Convert s to a list of repetitions for us to manipulate
        # For s = '11aaabB' we have groups = [2, 3, 1, 1]
        groups = [len(list(grp)) for _, grp in itertools.groupby(s)]
        
        # We apply deletions iteratively and always choose the best one.
        # This should be fine for short passwords :)
        # A delete is better the closer it gets us to removing a group of three.
        # Thus, a group needs to be (a) larger than 3 and (b) minimal wrt modulo 3.
        def apply_best_delete():
            argmin, _ = min(
                enumerate(groups),
                # Ignore groups of length < 3 as long as others are available.
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            groups[argmin] -= 1
        
        for _ in range(num_required_deletes):
            apply_best_delete()
        
        # On the finished groups, we need one repace per 3 consecutive letters.
        num_required_group_replaces = sum(
            group // 3
            for group in groups
        )
        
        return (
            # Deletes need to be done anyway
            num_required_deletes
            # Type replaces can be eaten up by inserts or group replaces.
            # Note that because of the interplay of rules (1) and (2), the required number of group replaces
            # can never be greater than the number of type replaces and inserts for candidates of length < 6.
            + max(
                num_required_type_replaces,
                num_required_group_replaces,
                num_required_inserts,
            )
        )
