class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_dict = {}

        for str in range(len(strs)):
            main_dict[str] = {}
            for x in strs[str]:
                main_dict[str][x] = main_dict[str].get(x,0) +1

        # main_dict
        output = []
        for key in main_dict:
            temp = []
            for k in main_dict:
                if main_dict[k] == main_dict[key]:
                    temp.append(strs[k])
            if not temp in output:        
                output.append(temp)
        return output