#1472. Design Browser History
#Medium
#
#You have a browser of one tab where you start on the homepage and you can visit another url,
#get back in the history number of steps or move forward in the history number of steps.
#
#Implement the BrowserHistory class:
#    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
#    void visit(string url) Visits url from the current page. It clears up all the forward history.
#    string back(int steps) Move steps back in history. If you can only return x steps in the
#        history and steps > x, you will return only x steps. Return the current url after
#        moving back in history at most steps.
#    string forward(int steps) Move steps forward in history. If you can only forward x steps
#        in the history and steps > x, you will forward only x steps. Return the current url
#        after forwarding in history at most steps.
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
#    homepage and url consist of  '.' or lower case English letters.
#    At most 5000 calls will be made to visit, back, and forward.

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # Clear forward history
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]
