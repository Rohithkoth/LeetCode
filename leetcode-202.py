class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            sumd = 0
            while n>0:
                sumd += (n%10)**2
                n = n//10
            if sumd in visited:
                return False
            n=sumd
            
        print(visited)
        return True