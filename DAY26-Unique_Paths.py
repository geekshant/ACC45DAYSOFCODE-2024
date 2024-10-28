def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]

def main():
    # Take input from the user
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))
    
    # Calculate the number of unique paths
    result = unique_paths(m, n)
    
    print(f"The number of unique paths in a {m}x{n} grid is: {result}")

if __name__ == "__main__":
    main()
