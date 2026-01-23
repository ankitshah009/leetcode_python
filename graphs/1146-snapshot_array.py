#1146. Snapshot Array
#Medium
#
#Implement a SnapshotArray that supports the following interface:
#    SnapshotArray(int length) initializes an array-like data structure with
#    the given length. Initially, each element equals 0.
#    void set(index, val) sets the element at the given index to be equal to val.
#    int snap() takes a snapshot of the array and returns the snap_id: the
#    total number of times we called snap() minus 1.
#    int get(index, snap_id) returns the value at the given index, at the
#    time we took the snapshot with the given snap_id
#
#Example 1:
#Input: ["SnapshotArray","set","snap","set","get"]
#[[3],[0,5],[],[0,6],[0,0]]
#Output: [null,null,0,null,5]
#Explanation:
#SnapshotArray snapshotArr = new SnapshotArray(3);
#snapshotArr.set(0,5);  // Set array[0] = 5
#snapshotArr.snap();    // Take a snapshot, return snap_id = 0
#snapshotArr.set(0,6);
#snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
#
#Constraints:
#    1 <= length <= 5 * 10^4
#    0 <= index < length
#    0 <= val <= 10^9
#    0 <= snap_id < (the total number of times we call snap())
#    At most 5 * 10^4 calls will be made to set, snap, and get.

import bisect

class SnapshotArray:
    """
    Store history of (snap_id, value) for each index.
    Use binary search for get.
    """
    def __init__(self, length: int):
        # For each index, store list of (snap_id, value)
        self.history = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1][1] = val
        else:
            self.history[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Binary search for largest snap_id <= given snap_id
        hist = self.history[index]
        pos = bisect.bisect_right(hist, [snap_id, float('inf')]) - 1
        return hist[pos][1]


class SnapshotArrayDict:
    """Alternative using dict for sparse updates"""
    def __init__(self, length: int):
        self.changes = [{0: 0} for _ in range(length)]  # index -> {snap_id: val}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.changes[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.changes[index]
        # Find latest snap_id <= given
        while snap_id >= 0 and snap_id not in snaps:
            snap_id -= 1
        return snaps.get(snap_id, 0)
