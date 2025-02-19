class Solution:
  def __init__(self):
      self.cache = {}


  def climbStairs(self, n):
      if n <= 3:
          return n
      if n in self.cache:
          return self.cache[n]
      self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
      return self.cache[n]
 