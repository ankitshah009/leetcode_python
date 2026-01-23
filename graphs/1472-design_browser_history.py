#1472. Design Browser History
#Medium
#
#You have a browser of one tab where you start on the homepage and you can
#visit another url, get back in the history number of steps or move forward
#in the history number of steps.
#
#Implement the BrowserHistory class:
#    BrowserHistory(string homepage) Initializes the object with the homepage
#    of the browser.
#
#    void visit(string url) Visits url from the current page. It clears up all
#    the forward history.
#
#    string back(int steps) Move steps back in history. If you can only return
#    x steps in the history and steps > x, you will return only x steps. Return
#    the current url after moving back in history at most steps.
#
#    string forward(int steps) Move steps forward in history. If you can only
#    forward x steps in the history and steps > x, you will forward only x steps.
#    Return the current url after forwarding in history at most steps.
#
#Example 1:
#Input:
#["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
#[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
#Output:
#[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
#
#Constraints:
#    1 <= homepage.length <= 20
#    1 <= url.length <= 20
#    1 <= steps <= 100
#    homepage and url consist of '.' or lower case English letters.
#    At most 5000 calls will be made to visit, back, and forward.

class BrowserHistory:
    """
    List-based implementation with current pointer.
    """

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # Clear forward history and add new url
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        # Move back at most 'steps' positions
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward at most 'steps' positions
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


class BrowserHistoryTwoStacks:
    """
    Two-stack implementation: back_stack and forward_stack.
    """

    def __init__(self, homepage: str):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack = []  # Clear forward history

    def back(self, steps: int) -> str:
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1
        return self.current


class ListNode:
    """Doubly linked list node for browser history"""
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistoryLinkedList:
    """
    Doubly linked list implementation.
    """

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url


class BrowserHistoryOptimized:
    """
    List with length tracking (avoids slicing).
    """

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0
        self.length = 1  # Actual valid length

    def visit(self, url: str) -> None:
        self.current += 1
        if self.current == len(self.history):
            self.history.append(url)
        else:
            self.history[self.current] = url
        self.length = self.current + 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.length - 1, self.current + steps)
        return self.history[self.current]
