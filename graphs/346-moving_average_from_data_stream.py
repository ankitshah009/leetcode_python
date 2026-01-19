#346. Moving Average from Data Stream
#Easy
#
#Given a stream of integers and a window size, calculate the moving average of
#all integers in the sliding window.
#
#Implement the MovingAverage class:
#- MovingAverage(int size) Initializes the object with the size of the window
#  size.
#- double next(int val) Returns the moving average of the last size values of
#  the stream.
#
#Example 1:
#Input: ["MovingAverage", "next", "next", "next", "next"]
#       [[3], [1], [10], [3], [5]]
#Output: [null, 1.0, 5.5, 4.66667, 6.0]
#
#Explanation:
#MovingAverage movingAverage = new MovingAverage(3);
#movingAverage.next(1); // return 1.0 = 1 / 1
#movingAverage.next(10); // return 5.5 = (1 + 10) / 2
#movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
#movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
#
#Constraints:
#    1 <= size <= 1000
#    -10^5 <= val <= 10^5
#    At most 10^4 calls will be made to next.

from collections import deque

class MovingAverage:
    """Using deque for O(1) operations"""

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        # Add new value
        self.window.append(val)
        self.window_sum += val

        # Remove oldest if window exceeds size
        if len(self.window) > self.size:
            self.window_sum -= self.window.popleft()

        return self.window_sum / len(self.window)


class MovingAverageCircular:
    """Using circular array"""

    def __init__(self, size: int):
        self.size = size
        self.array = [0] * size
        self.head = 0
        self.count = 0
        self.window_sum = 0

    def next(self, val: int) -> float:
        if self.count < self.size:
            self.count += 1
        else:
            # Remove oldest value from sum
            self.window_sum -= self.array[self.head]

        # Add new value
        self.array[self.head] = val
        self.window_sum += val
        self.head = (self.head + 1) % self.size

        return self.window_sum / self.count


class MovingAverageList:
    """Simple list-based approach"""

    def __init__(self, size: int):
        self.size = size
        self.window = []

    def next(self, val: int) -> float:
        self.window.append(val)
        if len(self.window) > self.size:
            self.window.pop(0)
        return sum(self.window) / len(self.window)
