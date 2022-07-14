class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs :
            return ""
        elif len(strs) == 1 :
            return strs[0]
        
        strs.sort(key=len)
        result = ""
        
        for i in range(len(strs[0])) :
            prefix = strs[0][i]
            
            for j in range(1, len(strs)) :
                if prefix == strs[j][i] :
                    if j == len(strs) - 1 :
                        result += prefix
                    continue
                return result
        return result