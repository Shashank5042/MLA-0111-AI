class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        self.moves = []

    def is_valid_move(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def is_dirty(self, x, y):
        return self.is_valid_move(x, y) and self.grid[x][y] == 'D'

    def clean_cell(self, x, y):
        if self.is_valid_move(x, y):
            self.grid[x][y] = 'C'

    def dfs(self, x, y):
        if not self.is_valid_move(x, y) or (x, y) in self.visited:
            return False
        
        self.visited.add((x, y))
        self.clean_cell(x, y)
        self.moves.append((x, y))

        if all(cell == 'C' for row in self.grid for cell in row):
            return True
        
        # Try moving in all four directions
        if self.dfs(x + 1, y) or self.dfs(x - 1, y) or self.dfs(x, y + 1) or self.dfs(x, y - 1):
            return True
        
        # If no solution found, backtrack
        self.clean_cell(x, y)
        self.moves.pop()
        return False

    def clean_grid(self):
        start_x, start_y = 0, 0
        self.dfs(start_x, start_y)

    def print_moves(self):
        print("Moves to clean all dirty cells:")
        for move in self.moves:
            print(move)

# Example usage:
grid = [
    ['C', 'D', 'C', 'C'],
    ['C', 'C', 'D', 'C'],
    ['C', 'C', 'C', 'C']
]

vacuum_cleaner = VacuumCleaner(grid)
vacuum_cleaner.clean_grid()
vacuum_cleaner.print_moves()
