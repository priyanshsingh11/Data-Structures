from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        need=Counter(t)
        miss=len(t)
        i,I,J=0,0,0

        for p,q in enumerate(s,1):
            miss-=need[q]>0
            need[q]-=1
            if not miss:
                while i<p and need[s[i]]<0:
                    need[s[i]]+=1
                    i+=1

                if J==0 or J-I>p-i:
                    I,J=i,p

        return s[I:J]
        
