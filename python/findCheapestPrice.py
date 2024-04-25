from collections import defaultdict, deque

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Create a graph from flights
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Initialize the cost to reach each node
        cost = [float('inf')] * n
        cost[src] = 0

        # Initialize a queue with (node, cost)
        q = deque()
        q.append((src, 0))
        stops = 0
        # BFS with stops constraint
        while q and stops <= k:
            for _ in range(len(q)):
                node, curr_cost = q.popleft()

                # Explore neighbors
                for nxt, nxt_cost in graph[node]:
                    new_cost = curr_cost + nxt_cost
                    # Get the min cost to reach each node
                    if new_cost < cost[nxt]:
                        cost[nxt] = new_cost
                        q.append((nxt, new_cost))
            stops += 1
        return cost[dst] if cost[dst] != float('inf') else -1


Solution().findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1)




