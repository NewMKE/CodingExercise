class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        a,b=1,2
        for _ in range(2,n):
            a, b = b, a+b
        return b


or:
class Solution:        
   def climbStairs(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        st = [0 for i in range(n)]
        st[0],st[1]=1,2
        for i in range(2,n):
            st[i]=st[i-1]+st[i-2]
        return st[-1]    # why are we using -1 instead of i here
        
        
if __name__=='__main__':
  s=Solution()
  print(s.climbStairs(5))
