class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = collections.defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        minHeap = [(0, 0)]
        visit = set()
        res = 0
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res += cost
            for next_cost, nei in graph[node]:
                heapq.heappush(minHeap, (next_cost, nei))
        return res