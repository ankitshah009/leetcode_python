#1665. Minimum Initial Energy to Finish Tasks
#Hard
#
#You are given an array tasks where tasks[i] = [actuali, minimumi]:
#
#    actuali is the actual amount of energy you spend to finish the ith task.
#    minimumi is the minimum amount of energy you require to begin the ith task.
#
#For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.
#
#You can finish the tasks in any order you like.
#
#Return the minimum initial amount of energy you will need to finish all the tasks.
#
# 
#
#Example 1:
#
#Input: tasks = [[1,2],[2,4],[4,8]]
#Output: 8
#Explanation:
#Starting with 8 energy, we finish the tasks in the following order:
#    - 3rd task. Now energy = 8 - 4 = 4.
#    - 2nd task. Now energy = 4 - 2 = 2.
#    - 1st task. Now energy = 2 - 1 = 1.
#Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.
#
#Example 2:
#
#Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
#Output: 32
#Explanation:
#Starting with 32 energy, we finish the tasks in the following order:
#    - 1st task. Now energy = 32 - 1 = 31.
#    - 2nd task. Now energy = 31 - 2 = 29.
#    - 3rd task. Now energy = 29 - 10 = 19.
#    - 4th task. Now energy = 19 - 10 = 9.
#    - 5th task. Now energy = 9 - 8 = 1.
#
#Example 3:
#
#Input: tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
#Output: 27
#Explanation:
#Starting with 27 energy, we finish the tasks in the following order:
#    - 5th task. Now energy = 27 - 5 = 22.
#    - 2nd task. Now energy = 22 - 2 = 20.
#    - 3rd task. Now energy = 20 - 3 = 17.
#    - 1st task. Now energy = 17 - 1 = 16.
#    - 4th task. Now energy = 16 - 4 = 12.
#    - 6th task. Now energy = 12 - 6 = 6.
#
# 

#Constraints:
#
#    1 <= tasks.length <= 105
#    1 <= actual​i <= minimumi <= 104




class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        min_energy=sum([i[0] for i in tasks])
        tasks1=sorted(tasks, key=lambda x: x[0],reverse=True)
        print(tasks1)
        min_energy_orig=min_energy
        for i in range(len(tasks1)):
            print(i,min_energy_orig)
            if min_energy >= tasks1[i][1]:
                min_energy = min_energy - tasks1[i][0]
                if (i+1<len(tasks1)) and (min_energy >= tasks1[i+1][1]):
                    print("HERE - if")
                    continue
                elif (i+1 < len(tasks1)) and (min_energy < tasks1[i+1][1]):
                    print("HERE1 - if")
                    min_energy_orig = min_energy_orig + (tasks1[i+1][1] - min_energy)
                    min_energy = tasks1[i+1][1]
                if i==len(tasks1)-1:
                    if min_energy >=0:
                        return min_energy_orig - min_energy
                    else:
                        return min_energy_orig + abs(min_energy)
            else:
                min_energy_orig = min_energy_orig + (tasks1[i][1]-min_energy)
                print(min_energy_orig)
                min_energy  = min_energy_orig - tasks1[i][0]
                #print(min_energy)
                if (i+1<len(tasks1)) and (min_energy >= tasks1[i+1][1]):
                    #print("HERE")
                    continue
                elif (i+1 < len(tasks1)) and (min_energy < tasks1[i+1][1]):
                    #print("HERE1")
                    min_energy_orig = min_energy_orig + (tasks1[i+1][1] - min_energy)
                    min_energy = tasks1[i+1][1]
                else:
                    if min_energy >= 0:
                        return min_energy_orig - min_energy
                    else:
                        return min_energy_orig + abs(min_energy)

#Approach #1 - Binary Search
#
#    Sort by difference
#    Use binary search validate if given input (energy) can finish all works
#    Search the smallest possible (like bisect_left)


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0]-x[1])
        def ok(mid):
            for actual, minimum in tasks:
                if minimum > mid or actual > mid: return False
                if minimum <= mid: mid -= actual
            return True
        l, r = 0, 10 ** 9
        while l <= r:
            mid = (l+r) // 2
            if ok(mid): r = mid - 1
            else: l = mid + 1
        return l
#Approach #2 - Greedy
#
#    Sort by difference
#    cur: actual cost, ans adjust by minimum so that it can start for all works


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0]-x[1])
        ans = cur = 0
        for cost, minimum in tasks:
            ans = min(cur-minimum, ans)
            cur -= cost
        return -ans

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: [x[0]-x[1],-x[1],x[0]])
        energy=0
        energyTotal=0
        for a,b in tasks:
            e=energy-b
            if e<0:
                energy-=e
                energyTotal-=e
            energy-=a
            
        return energyTotal
