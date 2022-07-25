class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)
        answer = len(arr)
        
        for i in range(len(arr)) :
            if arr[i] == heights[i] :
                answer -= 1
        
        return answer