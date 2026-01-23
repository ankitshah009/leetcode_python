#1115. Print FooBar Alternately
#Medium
#
#Suppose you are given the following code:
#
#class FooBar {
#  public void foo() {
#    for (int i = 0; i < n; i++) {
#      print("foo");
#    }
#  }
#  public void bar() {
#    for (int i = 0; i < n; i++) {
#      print("bar");
#    }
#  }
#}
#
#The same instance of FooBar will be passed to two different threads:
#    thread A will call foo(), while
#    thread B will call bar().
#
#Modify the given program to output "foobar" n times.
#
#Example 1:
#Input: n = 1
#Output: "foobar"
#
#Example 2:
#Input: n = 2
#Output: "foobarfoobar"
#
#Constraints:
#    1 <= n <= 1000

from typing import Callable
import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_done = threading.Event()
        self.bar_done = threading.Event()
        self.bar_done.set()  # Start with foo enabled

    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            self.bar_done.wait()
            self.bar_done.clear()
            printFoo()
            self.foo_done.set()

    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            self.foo_done.wait()
            self.foo_done.clear()
            printBar()
            self.bar_done.set()


class FooBarSemaphore:
    """Using semaphores"""
    def __init__(self, n):
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)

    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            self.foo_sem.acquire()
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            self.bar_sem.acquire()
            printBar()
            self.foo_sem.release()


class FooBarLock:
    """Using locks"""
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()
