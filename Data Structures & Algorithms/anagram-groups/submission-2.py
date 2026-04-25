class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            ss = "".join(sorted(s))
            dict[ss] = dict.get(ss,[])
            dict[ss].append(s)
        return list(dict.values())