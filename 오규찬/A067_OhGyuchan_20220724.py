class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        i = 0
        while i < len(s):
            if len(st)!=0 and st[-1]==s[i]:
                i+=1
                st.pop(-1)
            else:
                st.append(s[i])
                i+=1
        return "".join(i for i in st)