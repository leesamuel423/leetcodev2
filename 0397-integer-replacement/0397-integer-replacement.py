class Solution:
    def integerReplacement(self, n: int) -> int:
        cache = {}
        return self.helper(n, cache)


    def helper(self, n, cache):
        if n == 1:
            return 0
        if n in cache:
            return cache[n]
        
        if n % 2 == 0:
            cache[n] = 1 + self.helper(n // 2, cache)
        else:
            cache[n] = 1 + min(self.helper(n + 1, cache), self.helper(n - 1, cache))
        return cache[n]

 