class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        output = []
        # frequency count
        for x in nums:
            dict[x] = dict.get(x,0)+1
        # sorting
        sorted_items = sorted(dict.items(), key=lambda x: x[1],reverse=True)
        output = [key for key, value in sorted_items]
        return output[:k]      
         