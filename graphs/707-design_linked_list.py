#707. Design Linked List
#Medium
#
#Design your implementation of the linked list. You can choose to use a singly
#or doubly linked list.
#
#A node in a singly linked list should have two attributes: val and next.
#val is the value of the current node, and next is a pointer/reference to the
#next node.
#
#If you want to use the doubly linked list, you will need one more attribute
#prev to indicate the previous node in the linked list. Assume all nodes in
#the linked list are 0-indexed.
#
#Implement the MyLinkedList class:
#- MyLinkedList() Initializes the MyLinkedList object.
#- int get(int index) Get the value of the indexth node in the linked list.
#  If the index is invalid, return -1.
#- void addAtHead(int val) Add a node of value val before the first element.
#- void addAtTail(int val) Append a node of value val as the last element.
#- void addAtIndex(int index, int val) Add a node of value val before the
#  indexth node in the linked list.
#- void deleteAtIndex(int index) Delete the indexth node in the linked list.
#
#Example 1:
#Input: ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
#        "deleteAtIndex", "get"]
#       [[], [1], [3], [1, 2], [1], [1], [1]]
#Output: [null, null, null, null, 2, null, 3]
#
#Constraints:
#    0 <= index, val <= 1000
#    Please do not use the built-in LinkedList library.
#    At most 2000 calls will be made to various methods.

class MyLinkedList:
    """Singly linked list with dummy head"""

    class ListNode:
        def __init__(self, val=0):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = self.ListNode()  # Dummy head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0

        curr = self.head
        for _ in range(index):
            curr = curr.next

        new_node = self.ListNode(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next
        self.size -= 1


class MyLinkedListDoubly:
    """Doubly linked list with dummy head and tail"""

    class ListNode:
        def __init__(self, val=0):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.ListNode()  # Dummy head
        self.tail = self.ListNode()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        # Choose direction based on index
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        self._add_after(self.head, val)

    def addAtTail(self, val: int) -> None:
        self._add_after(self.tail.prev, val)

    def _add_after(self, node, val: int) -> None:
        new_node = self.ListNode(val)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0

        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        self._add_after(curr, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev

        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1
