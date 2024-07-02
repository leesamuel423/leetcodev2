from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sort_count = sorted(count.items(), key=lambda x: x[1])
        print(sort_count)
        final = []

        while k > 0:
            num, val = sort_count.pop()
            final.append(num)
            k -= 1
        
        return final


        

        