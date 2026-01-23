#1116. Print Zero Even Odd
#Medium
#
#You have a function printNumber that can be called with an integer parameter
#and prints it to the console.
#
#For example, calling printNumber(7) prints 7 to the console.
#
#You are given an instance of the class ZeroEvenOdd that has three functions:
#zero, even, and odd. The same instance of ZeroEvenOdd will be passed to
#three different threads:
#    Thread A: calls zero() that should only output 0's.
#    Thread B: calls even() that should only output even numbers.
#    Thread C: calls odd() that should only output odd numbers.
#
#Modify the given class to output the series "010203040506..." where the
#length of the series must be 2n.
#
#Example 1:
#Input: n = 2
#Output: "0102"
#
#Example 2:
#Input: n = 5
#Output: "0102030405"
#
#Constraints:
#    1 <= n <= 1000

from typing import Callable
import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sem = threading.Semaphore(1)
        self.odd_sem = threading.Semaphore(0)
        self.even_sem = threading.Semaphore(0)

    def zero(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.odd_sem.release()
            else:
                self.even_sem.release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()


class ZeroEvenOddEvent:
    """Using events"""
    def __init__(self, n):
        self.n = n
        self.zero_event = threading.Event()
        self.odd_event = threading.Event()
        self.even_event = threading.Event()
        self.zero_event.set()

    def zero(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1):
            self.zero_event.wait()
            self.zero_event.clear()
            printNumber(0)
            if i % 2 == 1:
                self.odd_event.set()
            else:
                self.even_event.set()

    def even(self, printNumber: Callable[[int], None]) -> None:
        for i in range(2, self.n + 1, 2):
            self.even_event.wait()
            self.even_event.clear()
            printNumber(i)
            self.zero_event.set()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_event.wait()
            self.odd_event.clear()
            printNumber(i)
            self.zero_event.set()
