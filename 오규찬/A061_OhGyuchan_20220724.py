class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ''
        while columnNumber != 0:
            tmp = chr(ord('A') + (columnNumber - 1) % 26)
            columnNumber = (columnNumber - 1) // 26
            answer = tmp + answer
        return answer