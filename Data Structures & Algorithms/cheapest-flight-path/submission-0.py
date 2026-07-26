class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in flights:
            edges[u].append((v, w))

        minHeap = [(0 , src, 0)] #(cost, city, edges)

        while minHeap:
            cost, city, edges_used = heapq.heappop(minHeap)

            if city == dst:
                return cost
            for nei, price in edges[city]:
                if edges_used < k + 1:
                    heapq.heappush(minHeap, (cost+price, nei, edges_used + 1))
        return -1