#2621. Sleep
#Easy
#
#Given a positive integer millis, write an asynchronous function that sleeps for millis
#milliseconds. It can resolve any value.
#
#Example 1:
#Input: millis = 100
#Output: 100
#Explanation: It should return a promise that resolves after 100ms.
#let t = Date.now();
#sleep(100).then(() => {
#  console.log(Date.now() - t); // 100
#});
#
#Example 2:
#Input: millis = 200
#Output: 200
#Explanation: It should return a promise that resolves after 200ms.
#
#Constraints:
#    1 <= millis <= 1000
#
#Note: This is a JavaScript problem. Python equivalent using asyncio is shown below.

import asyncio

async def sleep(millis: int) -> None:
    """
    Async function that sleeps for the specified milliseconds.
    """
    await asyncio.sleep(millis / 1000)

# Alternative using time module for synchronous sleep
import time

def sleep_sync(millis: int) -> None:
    """
    Synchronous function that sleeps for the specified milliseconds.
    """
    time.sleep(millis / 1000)
