#379. Design Phone Directory
#Medium
#
#Design a phone directory that initially has maxNumbers empty slots that can
#store numbers. The directory should store numbers, check if a certain slot is
#empty or not, and empty a given slot.
#
#Implement the PhoneDirectory class:
#- PhoneDirectory(int maxNumbers) Initializes the phone directory with the
#  number of available slots maxNumbers.
#- int get() Provides a number that is not assigned to anyone. Returns -1 if
#  no number is available.
#- bool check(int number) Returns true if the slot number is available and
#  false otherwise.
#- void release(int number) Recycles or releases the slot number.
#
#Example 1:
#Input: ["PhoneDirectory", "get", "get", "check", "get", "check", "release",
#        "check"]
#       [[3], [], [], [2], [], [2], [2], [2]]
#Output: [null, 0, 1, true, 2, false, null, true]
#
#Constraints:
#    1 <= maxNumbers <= 10^4
#    0 <= number < maxNumbers
#    At most 2 * 10^4 calls will be made to get, check, and release.

class PhoneDirectory:
    """Using set for O(1) operations"""

    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        if self.available:
            return self.available.pop()
        return -1

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        self.available.add(number)


class PhoneDirectoryQueue:
    """Using queue with availability tracking"""

    def __init__(self, maxNumbers: int):
        from collections import deque
        self.queue = deque(range(maxNumbers))
        self.is_available = [True] * maxNumbers

    def get(self) -> int:
        if self.queue:
            number = self.queue.popleft()
            self.is_available[number] = False
            return number
        return -1

    def check(self, number: int) -> bool:
        return self.is_available[number]

    def release(self, number: int) -> None:
        if not self.is_available[number]:
            self.is_available[number] = True
            self.queue.append(number)


class PhoneDirectoryLinkedList:
    """Using doubly linked list for O(1) get"""

    def __init__(self, maxNumbers: int):
        self.next_available = list(range(1, maxNumbers + 1))
        self.next_available[-1] = -1
        self.head = 0
        self.is_available = [True] * maxNumbers

    def get(self) -> int:
        if self.head == -1:
            return -1

        number = self.head
        self.head = self.next_available[number]
        self.is_available[number] = False
        return number

    def check(self, number: int) -> bool:
        return self.is_available[number]

    def release(self, number: int) -> None:
        if not self.is_available[number]:
            self.is_available[number] = True
            self.next_available[number] = self.head
            self.head = number
