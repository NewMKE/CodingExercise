class Solution:
    def square_sum(self, num):
        s = 0
        while num > 0:
            a = num % 10
            num = num // 10
            s = s + a ** 2
        return s

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        st = set()
        while not (n == 1 or n in st):
            st.add(n)
            n = self.square_sum(n)
        return n == 1


if __name__=='__main__':
    s=Solution()
    print(s.isHappy(19))
