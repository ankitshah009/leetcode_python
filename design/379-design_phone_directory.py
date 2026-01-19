#379. Design Phone Directory
#Medium
#
#Design a phone directory that initially has maxNumbers empty slots that can
#store numbers. The directory should store numbers, check if a certain slot is
#empty or not, and empty a given slot.
#
#Implement the PhoneDirectory class:
#    PhoneDirectory(int maxNumbers) Initializes the phone directory with the
#    number of available slots maxNumbers.
#    int get() Provides a number that is not assigned to anyone. Returns -1 if
#    no number is available.
#    bool check(int number) Returns true if the slot number is available and
#    false otherwise.
#    void release(int number) Recycles or releases the slot number.
#
#Example 1:
#Input
#["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
#[[3], [], [], [2], [], [2], [2], [2]]
#Output
#[null, 0, 1, true, 2, false, null, true]
#
#Explanation
#PhoneDirectory phoneDirectory = new PhoneDirectory(3);
#phoneDirectory.get();      // It can return any available phone number.
#phoneDirectory.get();      // Assume it returns 1.
#phoneDirectory.check(2);   // The number 2 is available, so return true.
#phoneDirectory.get();      // It returns 2.
#phoneDirectory.check(2);   // The number 2 is no longer available, return false.
#phoneDirectory.release(2); // Release number 2 back to the pool.
#phoneDirectory.check(2);   // Number 2 is available again, return true.
#
#Constraints:
#    1 <= maxNumbers <= 10^4
#    0 <= number < maxNumbers
#    At most 2 * 10^4 calls will be made to get, check, and release.

class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        if not self.available:
            return -1
        return self.available.pop()

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        self.available.add(number)


class PhoneDirectoryQueue:
    """Using deque for more deterministic get() behavior"""

    def __init__(self, maxNumbers: int):
        from collections import deque
        self.available_queue = deque(range(maxNumbers))
        self.available_set = set(range(maxNumbers))

    def get(self) -> int:
        if not self.available_queue:
            return -1
        number = self.available_queue.popleft()
        self.available_set.remove(number)
        return number

    def check(self, number: int) -> bool:
        return number in self.available_set

    def release(self, number: int) -> None:
        if number not in self.available_set:
            self.available_set.add(number)
            self.available_queue.append(number)


class PhoneDirectoryBitset:
    """Using bitset for memory efficiency"""

    def __init__(self, maxNumbers: int):
        self.max_numbers = maxNumbers
        self.bitset = (1 << maxNumbers) - 1  # All bits set to 1
        self.next_available = 0

    def get(self) -> int:
        if self.bitset == 0:
            return -1

        # Find the next available number
        while self.next_available < self.max_numbers:
            if self.bitset & (1 << self.next_available):
                number = self.next_available
                self.bitset &= ~(1 << number)  # Mark as used
                return number
            self.next_available += 1

        # Reset and search from beginning
        self.next_available = 0
        while self.next_available < self.max_numbers:
            if self.bitset & (1 << self.next_available):
                number = self.next_available
                self.bitset &= ~(1 << number)
                return number
            self.next_available += 1

        return -1

    def check(self, number: int) -> bool:
        return bool(self.bitset & (1 << number))

    def release(self, number: int) -> None:
        self.bitset |= (1 << number)
