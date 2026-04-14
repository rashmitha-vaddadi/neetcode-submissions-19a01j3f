class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False] * len(strs)
        result = []

        for i in range(len(strs)):
            if visited[i]:
                continue                      # already grouped, skip
            group = [strs[i]]
            for j in range(i + 1, len(strs)):
                if not visited[j] and self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited[j] = True         # mark so it's not re-grouped
            result.append(group)

        return result

    def isAnagram(self, s1, s2) -> bool:
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)       # sorted() not is.sorted()
        