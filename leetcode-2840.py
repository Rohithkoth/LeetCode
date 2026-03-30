class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = {}
        odd = {}
        even2 = {}
        odd2 = {}


        for i in range(len(s1)):
            if i % 2 == 0:
                if s1[i] not in even:
                    even[s1[i]] = 1
                else:
                    even[s1[i]] = even[s1[i]] +1
            
                if s2[i] not in even2:
                    even2[s2[i]] = 1
                else:
                    even2[s2[i]] = even2[s2[i]] +1
            
            
            else:
                if s1[i] not in odd:
                    odd[s1[i]] = 1
                else:
                    odd[s1[i]] = odd[s1[i]] +1

                if s2[i] not in odd2:
                    odd2[s2[i]] = 1
                else:
                    odd2[s2[i]] = odd2[s2[i]] +1

        print("odds")
        print(odd)
        print(odd2)
        print("evens")
        print(even)
        print(even2)
        return odd == odd2 and even == even2