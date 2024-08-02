class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        cache = {}
        for i in answers:
            if i == 0:
                count += 1
            elif i not in cache:
                cache[i] = i
            else:
                cache[i] -= 1
                print(cache)
                if cache[i] == 0:
                    count += (i + 1)
                    del cache[i]
        for i in cache.keys():
            count += (i + 1)
        return count
                


"""
[1, 1, 2]
red, red
blue, blue
3 + 2 = 5


[10, 10, 10]
how many other rabbits
11

1: 2
2: 3

"""
        