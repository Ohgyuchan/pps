class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for num in range(left, right + 1) :
            result = False
            for n in str(num) :
                temp = int(n)
                if temp == 0 : 
                    result = False
                    break
                elif num % temp == 0 :
                    result = True
                else :
                    result = False
                    break
            if result :
                answer.append(num)
        return answer