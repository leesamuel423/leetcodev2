class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        arr = list(range(1, n))
        arr2 = list(range(2, n + 1))[::-1]
        arr.extend(arr2)
        # print(arr)

        index = time if time <= len(arr) - 1 else time % len(arr)
        # print(index, arr[index])

        return arr[index]


"""
can use pointer to iterate through 1 - n array going right left until end
O(n) where n represents time

more efficient =>

1, 2, 3, 4

(n * 2) - 2 to get back to original person

1, 2, 3, 4, 3, 2
time = 12 expect 1

"""
        