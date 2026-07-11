class Solution:
    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=str(len(i))+"#"+i
        return result

    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            val=int(s[i:j])
            result.append(str(s[j+1:j+1+val]))
            i=j+1+val
        return result

