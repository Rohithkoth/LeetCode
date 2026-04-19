class Solution:
    def mirrorDistance(self, n: int) -> int:
        stringN = str(n)

        rev = ""
        for c in stringN:
            rev = c + rev

        rev = int(rev)

        return abs(n-rev)