from copy import deepcopy
class NQ:
    
    def __init__(self,n):
        self.n = n+1
        self.x = [i*0 for i in range(self.n)]
        self.solutions = []
        
    #N QUEEN ALGORITHM USING BACKTRACKING
        
    def Place(self,k,i):
        for j in range(1,k):
            if(self.x[j] == i or abs(self.x[j] - i) == abs(j-k)):
                return False
        return True

    def Nqueens(self,k):
        for i in range(1,self.n):
            if(self.Place(k,i)):
                self.x[k] = i
                if(k == self.n-1):
                    temp = deepcopy(self.x)
                    self.solutions.append(temp)
                self.Nqueens(k+1)
                