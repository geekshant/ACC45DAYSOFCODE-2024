def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = grid[0][0]
    
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    return dp[m - 1][n - 1]

def main():
    # Take input from the user
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))
    
    print(f"Enter the grid of size {m} x {n}, row by row:")
    grid = []
    for i in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # Calculate the minimum path sum
    result = min_path_sum(grid)
    
    print(f"The minimum path sum is: {result}")

if __name__ == "__main__":
    main()
