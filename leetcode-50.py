class Solution:
    def myPow(self, x: float, n: int) -> float:
        xorig = x
        if n>0:
            for _ in range(0,n-1):
                x*=xorig

        else:
            for _ in range(0,n-1,-1):
                x/=xorig
        return x