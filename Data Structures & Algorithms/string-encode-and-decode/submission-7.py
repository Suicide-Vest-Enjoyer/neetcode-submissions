class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for v in strs:
            result += f"#{len(v)}#{v}"
        return result 

    def decode(self, s: str) -> List[str]:
        to_read = 0
        result = []
        word = ""
        str_num = ""
        num = 0
        while True:
            if s == "":
                break
            s = s[1:]
            while True:
                if s[0] == "#":
                    s = s[1:]
                    num = int(str_num)
                    str_num = ""
                    break
                str_num += s[0]
                s = s[1:]
            for _ in range(num):
                word += s[0]
                s = s[1:]
            result.append(word)
            word = ""
        return result


