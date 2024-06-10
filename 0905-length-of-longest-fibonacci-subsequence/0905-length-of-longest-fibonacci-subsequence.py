class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_length = 0
        arr_set = set(arr)

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                local_length = 2
                while a + b in arr_set:
                    a, b = b, a + b
                    local_length += 1
                if local_length > 2 and local_length > max_length: 
                    max_length = local_length
        return max_length




        