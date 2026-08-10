#我有一点读不懂题
#NeetCode Solution 2 (similar to video version)

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j=i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # 把切出来的字符串转成整数，比如s[0:1] 中的数字4；只有这里拿到数字，之后才能做加法i+length
            i = j+1
            j = i+length
            res.append(s[i:j])
            i=j

        return res

            
