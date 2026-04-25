class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        # seen = [set() for _ in range(len(nums))]
        seen = []
        c =0
        for x in range(len(nums)):
            if not nums[x]-1 in hash_set :
                seen.append(set())
                seen[c].add(nums[x])
                c+=1
        print(seen)        

        for i in range(len(seen)):
            if seen[i]:
                x = seen[i].pop()
                while x in hash_set:
                    seen[i].add(x)
                    x+=1
        output = 0
        for i in seen:
            if len(i) > output:
                output = len(i)  
        return output        