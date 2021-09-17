class Solution :
    def generate(self, R, B, G) :
        L = []
        S = []
        def backtrack(R1,B1,G1,prev) :
            if R1==R and B1==B and G1==G :
                L.append("".join(S))
                return
            if R1<R and prev!='R' :
                S.append('R')
                backtrack(R1+1,B1,G1,'R')
                S.pop(len(S)-1)
            if B1<B and prev!='B' :
                S.append('B')
                backtrack(R1,B1+1,G1,'B')
                S.pop(len(S)-1)
            if G1<G and prev!='G' :
                S.append('G')
                backtrack(R1,B1,G1+1,'G')
                S.pop(len(S)-1)        
        backtrack(0,0,0,None) 
        print(L)
        print(len(L))

R,G,B = list(map(int, input("Enter R, G and B : ").split(" ")))
ob = Solution()
ob.generate(R,G,B)