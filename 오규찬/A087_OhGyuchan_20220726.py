class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        a = sorted(boxTypes, key = lambda x : -x[1])
        count = 0
        answer = 0
        for box, unit in a:
            count += box
            if count > truckSize:
                answer += (truckSize - (count - box)) * unit
                break
            answer += box * unit
        return answer