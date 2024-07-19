from collections import defaultdict

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)
    
    def dfs(self, rooms, room, visited):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
            self.dfs(rooms, key, visited)




    """
    visited set
    dfs starting 0
    return if length of visited is same as length of rooms
    
    helper function dfs
        if room in visited, return
        add to visited
        iterate through curr room
            dfs for keys
    """
        