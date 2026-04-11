class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for l in range(len(strs[0])):
            for r in strs:
                if l == len(r) or r[l] != strs[0][l]:
                    return res
            res += strs[0][l]
        return res


        