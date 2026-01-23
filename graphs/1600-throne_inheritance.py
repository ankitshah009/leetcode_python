#1600. Throne Inheritance
#Medium
#
#A kingdom consists of a king, his children, his grandchildren, and so on.
#Every once in a while, someone in the family dies or a child is born.
#
#The kingdom has a well-defined order of inheritance that consists of the king
#as the first member. Let's define the recursive function Successor(x, curOrder),
#which given a person x and the current inheritance order, returns who should
#be the next person after x in the order of inheritance.
#
#Successor(x, curOrder):
#    if x has no children or all of x's children are in curOrder:
#        if x is the king return null
#        else return Successor(x's parent, curOrder)
#    else return x's oldest child who's not in curOrder
#
#For example, assume we have a kingdom that consists of the king, his children
#Alice and Bob (Alice is older than Bob), and finally Alice's son Jack.
#
#In the beginning, curOrder will be ["king"].
#Calling Successor(king, curOrder) will return Alice, so we add Alice to curOrder.
#Calling Successor(Alice, curOrder) will return Jack, so we add Jack to curOrder.
#Calling Successor(Jack, curOrder) will return Bob, so we add Bob to curOrder.
#Calling Successor(Bob, curOrder) will return null.
#Thus the order of inheritance will be ["king", "Alice", "Jack", "Bob"].
#
#Using the above function, we can always obtain a unique order of inheritance.
#
#Implement the ThroneInheritance class:
#- ThroneInheritance(string kingName): Initializes an object with the king's name.
#- void birth(string parentName, string childName): Indicates that parentName
#  gave birth to childName.
#- void death(string name): Indicates the death of name. The death won't affect
#  the Successor function nor the current inheritance order.
#- string[] getInheritanceOrder(): Returns a list representing the current order
#  of inheritance excluding dead people.
#
#Example 1:
#Input:
#["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth",
# "getInheritanceOrder", "death", "getInheritanceOrder"]
#[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"],
# ["andy", "matthew"], ["andy", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
#Output:
#[null, null, null, null, null, null, null,
# ["king", "andy", "matthew", "alex", "bob", "asha", "catherine"],
# null,
# ["king", "andy", "matthew", "alex", "asha", "catherine"]]
#
#Constraints:
#    1 <= kingName.length, parentName.length, childName.length <= 15
#    kingName, parentName, and childName consist of lowercase English letters only.
#    All arguments childName and kingName are distinct.
#    All parentName to birth calls have existed in the inheritance tree.
#    At most 10^5 total calls will be made to birth and death.
#    At most 10 calls will be made to getInheritanceOrder.

from typing import List
from collections import defaultdict

class ThroneInheritance:
    """
    The inheritance order is essentially a pre-order DFS traversal of the family tree.
    - Parent before children
    - Older children before younger siblings
    """

    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)  # parent -> list of children (in birth order)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []

        def dfs(person: str):
            if person not in self.dead:
                result.append(person)
            for child in self.children[person]:
                dfs(child)

        dfs(self.king)
        return result


class ThroneInheritanceIterative:
    """
    Iterative DFS implementation.
    """

    def __init__(self, kingName: str):
        self.king = kingName
        self.family = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []
        stack = [self.king]

        while stack:
            person = stack.pop()

            if person not in self.dead:
                result.append(person)

            # Add children in reverse order so oldest is processed first
            for child in reversed(self.family[person]):
                stack.append(child)

        return result


class ThroneInheritanceNode:
    """
    Using node-based tree structure.
    """

    class Person:
        def __init__(self, name: str):
            self.name = name
            self.children = []
            self.is_dead = False

    def __init__(self, kingName: str):
        self.king = self.Person(kingName)
        self.people = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        child = self.Person(childName)
        self.people[parentName].children.append(child)
        self.people[childName] = child

    def death(self, name: str) -> None:
        self.people[name].is_dead = True

    def getInheritanceOrder(self) -> List[str]:
        result = []

        def preorder(person):
            if not person.is_dead:
                result.append(person.name)
            for child in person.children:
                preorder(child)

        preorder(self.king)
        return result
