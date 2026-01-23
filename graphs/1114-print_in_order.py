#1114. Print in Order
#Easy
#
#Suppose we have a class:
#
#public class Foo {
#  public void first() { print("first"); }
#  public void second() { print("second"); }
#  public void third() { print("third"); }
#}
#
#The same instance of Foo will be passed to three different threads. Thread A
#will call first(), thread B will call second(), and thread C will call
#third(). Design a mechanism and modify the program to ensure that second()
#is executed after first(), and third() is executed after second().
#
#Example 1:
#Input: nums = [1,2,3]
#Output: "firstsecondthird"
#Explanation: There are three threads being fired asynchronously. The input
#[1,2,3] means thread A calls first(), thread B calls second(), and thread C
#calls third(). "firstsecondthird" is the correct output.
#
#Example 2:
#Input: nums = [1,3,2]
#Output: "firstsecondthird"
#Explanation: The input [1,3,2] means thread A calls first(), thread B calls
#third(), and thread C calls second(). "firstsecondthird" is the correct output.
#
#Constraints:
#    nums is a permutation of [1, 2, 3].

from typing import Callable
import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond: Callable[[], None]) -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird: Callable[[], None]) -> None:
        self.second_done.wait()
        printThird()


class FooLock:
    """Using locks instead of events"""
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        self.lock1.release()

    def second(self, printSecond: Callable[[], None]) -> None:
        self.lock1.acquire()
        printSecond()
        self.lock2.release()

    def third(self, printThird: Callable[[], None]) -> None:
        self.lock2.acquire()
        printThird()


class FooCondition:
    """Using condition variable"""
    def __init__(self):
        self.condition = threading.Condition()
        self.order = 0

    def first(self, printFirst: Callable[[], None]) -> None:
        with self.condition:
            printFirst()
            self.order = 1
            self.condition.notify_all()

    def second(self, printSecond: Callable[[], None]) -> None:
        with self.condition:
            self.condition.wait_for(lambda: self.order == 1)
            printSecond()
            self.order = 2
            self.condition.notify_all()

    def third(self, printThird: Callable[[], None]) -> None:
        with self.condition:
            self.condition.wait_for(lambda: self.order == 2)
            printThird()
