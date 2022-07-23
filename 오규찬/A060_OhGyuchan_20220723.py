class Solution:
    def calPoints(self, ops: List[str]) -> int:
        answer = []
        
        for op in ops :
            if op=="C":
                answer.pop()
                
            elif op=="D":
                answer.append(2 * answer[-1])
                
            elif op=="+":
                answer.append(answer[-1] + answer[-2])
                
            else:
                answer.append(int(op))
        
        return sum(answer)