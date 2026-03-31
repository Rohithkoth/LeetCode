class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        mat2 = mat.copy()
        for _ in range(k):
            for m in range(len(mat)):
                if m %2 == 0:
                    mat2[m]=mat2[m][1:] + [mat2[m][0]]
                else:
                    mat2[m] = [mat2[m][-1]] + mat2[m][:-1]
        print(mat2)
        return mat2 == mat
