from functools import cache
class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        """
        case1
        n

        case 2
        .a: if next to . not  *, move i+1,j+1

        case 3
        .*x recurse on i, j+1 also recurse on i+2, j+1

        case 4
        n* recurse on i j+1 also i+2, j+1 
        case 5:
        
        case 6:
            s="a"
            p="ab*a*"
        """
        @cache
        def BT(i,j):
            if j>=len(p) and i<len(s):
                return False
            if j>=len(p) and i>=len(s):
                return True
            if j<len(p) and i>=len(s):# check if the rest is *a*b which can collapse to 0
                
                while j+1<len(p) and p[j+1]=='*':
                    j+=2
                if j<len(p):
                    return False
                return True
                
            

            res=False
            if s[i]==p[j]:#match n = n*
                if j+1<len(p) and p[j+1]=='*': #n = n*
                    res = BT(i+1,j) #use the *

                    res = res or BT(i,j+2)#not use *
                else:#n=n just a normal match
                    res= BT(i+1,j+1)

            elif p[j]=='.':
                if j+1<len(p) and p[j+1]=='*':
                    res = BT(i+1,j)
                    res = res or BT(i,j+2)#not use .
                else:#just a normal match
                    res= BT(i+1,j+1)

            elif j+1<len(p) and  p[j+1]=='*':#not a match but *, can use 0
                res=BT(i,j+2)


            return res
        return BT(0,0)


