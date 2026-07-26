class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        def isrotten(r, c):
            nonlocal fresh
            if (r < 0 or r >= rows or c < 0 or c >= cols
                or (r, c) in visit or grid[r][c] != 1):
                return
            grid[r][c] = 2
            fresh -= 1
            q.append((r, c))
            visit.add((r, c))

        minutes = -1
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                isrotten(r + 1, c)
                isrotten(r - 1, c)
                isrotten(r, c + 1)
                isrotten(r, c - 1)
            minutes += 1
        
        if fresh > 0:
            return -1
        else:
            return minutes
