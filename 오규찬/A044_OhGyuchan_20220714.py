class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = not s.count("A") >= 2
        late = True
        
        for i in range(len(s)) :
            if s[i] == "L" and len(s) - i + 1 >= 2:
                temp = s[i:i+3]
                if temp.count("L") == 3 :
                    late = False
                    
        return absent and late