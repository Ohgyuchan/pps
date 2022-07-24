class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            n_list = list(map(int,str(i)))
            flag = 1
            for j in range(len(n_list)):

                if n_list[j] == 0 or i % n_list[j] != 0:
                    flag = 0
                    break
            if flag == 1:
                ans.append(i)
                
        return ans
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        