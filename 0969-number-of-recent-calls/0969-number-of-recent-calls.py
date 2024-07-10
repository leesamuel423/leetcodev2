class RecentCounter:

    def __init__(self):
        self.queue = deque([])
    
    def ping(self, t):
        first = t - 3000
        second = t
        self.queue.append(second)
        while self.queue[0] < first:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)