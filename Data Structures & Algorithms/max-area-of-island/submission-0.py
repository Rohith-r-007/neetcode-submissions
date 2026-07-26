class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        max_area = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            area = 1
            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col

                    if ( r in range(rows) and c in range(cols)
                        and grid[r][c] == 1 and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, bfs(r, c))
        return max_area