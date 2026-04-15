class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False] * len(strs)
        ans = []
        for i in range(len(strs)):
            if visited[i]:
                continue
            
            # Mark the current element as visited immediately
            visited[i] = True 
            grp = [strs[i]]
            
            for j in range(i + 1, len(strs)):
                # If we find a match, mark the MATCHING element (j) as visited
                if not visited[j] and self.anagram(strs[i], strs[j]):
                    grp.append(strs[j])
                    visited[j] = True  # Changed from visited[i] to visited[j]
            
            ans.append(grp)
        return ans

    def anagram(self, s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)