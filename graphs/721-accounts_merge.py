#721. Accounts Merge
#Medium
#
#Given a list of accounts where each element accounts[i] is a list of strings,
#where the first element accounts[i][0] is a name, and the rest of the elements
#are emails representing emails of the account.
#
#Now, we would like to merge these accounts. Two accounts definitely belong to
#the same person if there is some common email to both accounts. Note that even
#if two accounts have the same name, they may belong to different people as
#people could have the same name. A person can have any number of accounts
#initially, but all of their accounts definitely have the same name.
#
#After merging the accounts, return the accounts in the following format: the
#first element of each account is the name, and the rest of the elements are
#emails in sorted order.
#
#Example 1:
#Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
#                   ["John","johnsmith@mail.com","john00@mail.com"],
#                   ["Mary","mary@mail.com"],
#                   ["John","johnnybravo@mail.com"]]
#Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#         ["Mary","mary@mail.com"],
#         ["John","johnnybravo@mail.com"]]
#
#Constraints:
#    1 <= accounts.length <= 1000
#    2 <= accounts[i].length <= 10
#    1 <= accounts[i][j].length <= 30
#    accounts[i][0] consists of English letters.
#    accounts[i][j] (for j > 0) is a valid email.

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """
        Union-Find: union all emails in same account, then group by root.
        """
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Build union-find structure
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        # Group emails by root
        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)

        # Build result
        result = []
        for root, emails in groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))

        return result


class SolutionDFS:
    """DFS on email graph"""

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Build graph: email -> set of connected emails
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if len(account) > 2:
                    graph[account[1]].add(email)
                    graph[email].add(account[1])

        # DFS to find connected components
        visited = set()
        result = []

        def dfs(email, emails):
            if email in visited:
                return
            visited.add(email)
            emails.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, emails)

        for email in email_to_name:
            if email not in visited:
                emails = []
                dfs(email, emails)
                result.append([email_to_name[email]] + sorted(emails))

        return result


class SolutionBFS:
    """BFS on email graph"""

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        from collections import deque

        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                graph[account[1]].add(email)
                graph[email].add(account[1])

        visited = set()
        result = []

        for email in email_to_name:
            if email not in visited:
                emails = []
                queue = deque([email])
                visited.add(email)

                while queue:
                    curr = queue.popleft()
                    emails.append(curr)

                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

                result.append([email_to_name[email]] + sorted(emails))

        return result
