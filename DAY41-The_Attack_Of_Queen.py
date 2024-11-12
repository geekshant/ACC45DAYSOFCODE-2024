def count_cells_under_attack(N, X, Y):
    # Vertical and horizontal cells
    vertical_and_horizontal = 2 * (N - 1)
    
    # Diagonal cells
    top_left_diagonal = min(X - 1, Y - 1)
    bottom_right_diagonal = min(N - X, N - Y)
    top_right_diagonal = min(X - 1, N - Y)
    bottom_left_diagonal = min(N - X, Y - 1)
    
    diagonal = top_left_diagonal + bottom_right_diagonal + top_right_diagonal + bottom_left_diagonal
    
    return vertical_and_horizontal + diagonal

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, X, Y = map(int, input("Enter N, X, and Y separated by spaces: ").split())
        results.append(count_cells_under_attack(N, X, Y))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
