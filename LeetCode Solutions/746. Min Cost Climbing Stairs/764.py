class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length=len(cost)
        f1 , f2 = cost[0], cost[1]
        for i in range(2,length):
            f1, f2 = f2, min(f1, f2)+cost[i]
        return min(f1, f2)


if __name__=='__main__':
    s=Solution()
    cost=[45,1,55,15,1,7]
    print(s.minCostClimbingStairs(cost))
