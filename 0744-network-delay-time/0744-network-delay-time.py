class Solution:
    def networkDelayTime(self, times, n, k):
        adj = self.create_adj(times)
        return self.dijkstra(adj, n, k)

    def create_adj(self, times):
        adj = defaultdict(list)
        for i in times:
            source, target, dist = i
            adj[source].append((target, dist))
        return adj

    def dijkstra(self, adj, n, k):
        heap = [(0, k)]
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
    
        while heap:
            current_dist, node = heapq.heappop(heap)
    
            if current_dist > dist[node]:
                continue
        
            for neighbor, weight in adj[node]:
                distance = current_dist + weight
        
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor)) 
                
        #         print("new: ", heap)
        #         print("new: ", dist)
                
        # print(dist.values())
        max_dist = max(dist.values())
        return max_dist if max_dist < float('inf') else -1



"""
create adj list
ie: {
    2: [(1, 1), (3, 1)],
    3: [(4, 1)]
}

visited set

bfs
queue = deque([(node, dist, max)])
    
return sum or -1
"""
    
            