#406. Queue Reconstruction by Height
#Medium
#
#You are given an array of people, people, which are the attributes of some people in a queue
#(not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi
#with exactly ki other people in front who have a height greater than or equal to hi.
#
#Reconstruct and return the queue that is represented by the input array people.
#The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the
#attributes of the jth person in the queue (queue[0] is the person at the front of the queue).
#
#Example 1:
#Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
#Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
#
#Example 2:
#Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
#Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
#
#Constraints:
#    1 <= people.length <= 2000
#    0 <= hi <= 10^6
#    0 <= ki < people.length
#    It is guaranteed that the queue can be reconstructed.

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, then by k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for person in people:
            result.insert(person[1], person)

        return result
