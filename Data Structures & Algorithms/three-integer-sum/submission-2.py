class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i, val in enumerate(nums):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l,r = i+1 , len(nums)-1
            while l<r:
                s = val + nums[l] + nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    temp = [val,nums[l],nums[r]]
                    if temp not in res:
                        res.append(temp)
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res
