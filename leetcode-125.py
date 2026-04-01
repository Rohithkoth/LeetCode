class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r =len(s)-1

        while l<r:
            print(s[l] + ' ' +s[r])
            if s[l] == ' ' or s[l] in "~!@#$%^&*()-_+={}[];'|:,.<>?": 
                l+=1
                
            if s[r] == ' ' or s[r] in "~!@#$%^&*()-_+={}[];'|:,.<>?": 
                r-=1
                
            if (s[r] == ' ' or s[r] in "~!@#$%^&*()-_+={}[];'|:,.<>?" or  s[l] == ' ' or s[l] in "~!@#$%^&*()-_+={}[];'|:,.<>?" ) == False:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l+=1
                    r-=1
        return True