#981. Time Based Key-Value Store
#Medium
#
#Design a time-based key-value data structure that can store multiple values for
#the same key at different time stamps and retrieve the key's value at a certain
#timestamp.
#
#Implement the TimeMap class:
#- TimeMap() Initializes the object of the data structure.
#- void set(String key, String value, int timestamp) Stores the key key with the
#  value value at the given time timestamp.
#- String get(String key, int timestamp) Returns a value such that set was called
#  previously, with timestamp_prev <= timestamp. If there are multiple such values,
#  it returns the value associated with the largest timestamp_prev. If there are
#  no values, it returns "".
#
#Example 1:
#Input
#["TimeMap", "set", "get", "get", "set", "get", "get"]
#[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
#Output
#[null, null, "bar", "bar", null, "bar2", "bar2"]
#
#Constraints:
#    1 <= key.length, value.length <= 100
#    key and value consist of lowercase English letters and digits.
#    1 <= timestamp <= 10^7
#    All the timestamps timestamp of set are strictly increasing.
#    At most 2 * 10^5 calls will be made to set and get.

from collections import defaultdict
import bisect

class TimeMap:
    """Using binary search on sorted timestamps"""

    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        # Binary search for largest timestamp <= given timestamp
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result


class TimeMapBisect:
    """Using bisect module"""

    def __init__(self):
        self.store = defaultdict(list)
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append(value)
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        times = self.timestamps[key]
        idx = bisect.bisect_right(times, timestamp)

        if idx == 0:
            return ""

        return self.store[key][idx - 1]


class TimeMapDict:
    """Using dict with list of tuples"""

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        values = self.data[key]

        # Since timestamps are strictly increasing, use binary search
        left, right = 0, len(values) - 1

        while left < right:
            mid = (left + right + 1) // 2
            if values[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1

        if values[left][0] <= timestamp:
            return values[left][1]
        return ""
