class Solution:
    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=str(len(i))+"#"+i
        return result

    def decode(self, s: str) -> List[str]:
        left=0
        result=[]
        while left<len(s):
            right=left
            while s[right]!="#":
                right+=1
            val=int(s[left:right])
            result.append(str(s[right+1:right+1+val]))
            left=right+1+val
        return result

class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"#"+i
        return res


    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            val=int(s[i:j])
            res.append(str(s[j+1:j+1+val]))
            i=j+1+val
        return res
