class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix)-1
        l=0
        r = len(matrix[0])-1

        while t<=b:
            m = (t+b)//2
            if matrix[m][0]>target:
                b = m-1
            elif matrix[m][r] < target:
                t = m +1
            else:
                while l <= r:
                    i = (r+l)//2
                    if matrix[m][i] > target:
                        r = i-1
                    elif matrix[m][i] < target:
                        l = i+1
                    else:
                        return True
                return False 