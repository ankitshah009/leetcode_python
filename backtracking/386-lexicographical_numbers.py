#386. Lexicographical Numbers
#Medium
#
#Given an integer n, return 1 - n in lexicographical order.
#
#For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
#Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = [0]*n
        num = 1        
        for i in range(n):
            ret[i] = num
            if num * 10 <=n :
                num = num * 10
            elif num + 1 <= n and num % 10 != 9:
                num = num + 1                
            else:
                num = num // 10 + 1
                while num % 10 == 0:
                    num = num // 10
        return ret
