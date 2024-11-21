def unguarded_cells(m, n, guards, walls):
    # Initialize the grid
    grid = [[0] * n for _ in range(m)]
    
    # Mark the positions of guards and walls
    for r, c in guards:
        grid[r][c] = 1  # Guard
    for r, c in walls:
        grid[r][c] = -1  # Wall

    # Directions: north, east, south, west
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Mark cells guarded by each guard
    for r, c in guards:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1 and grid[nr][nc] != 1:
                grid[nr][nc] = 2  # Guarded cell
                nr += dr
                nc += dc
    
    # Count unguarded cells
    unguarded_count = 0
    for row in grid:
        unguarded_count += row.count(0)
    
    return unguarded_count

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        m, n = map(int, input("Enter the dimensions of the grid (m n): ").split())
        num_guards = int(input("Enter the number of guards: "))
        guards = [list(map(int, input("Enter guard position: ").split())) for _ in range(num_guards)]
        num_walls = int(input("Enter the number of walls: "))
        walls = [list(map(int, input("Enter wall position: ").split())) for _ in range(num_walls)]
        
        results.append(unguarded_cells(m, n, guards, walls))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
