class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        
        def createSolutionMatrix(nSticks, nVisible):
            #N is greater than k or else the problem is invalid
            B = [[0 for i in range(nSticks)] for j in range(nSticks)]
            
            for n in range(nSticks):
                for k in range(n+1):
                    if k == n: B[k][n] = 1 #Exactly one way to make this arrangement
                    
                    #If K is one then there are exactly the total number of ways to solve the previous N level
                    # ways to solve this- add the new stick first and then any arrangement of n-1 sticks
                    elif k == 0: B[n][k] = sum(B[n-1])
                    
                    else: B[n][k] = (n) * B[n-1][k] + B[n-1][k-1]
            return B[nSticks-1][nVisible-1]%(10**9 + 7)
            
        return createSolutionMatrix(n,k)
