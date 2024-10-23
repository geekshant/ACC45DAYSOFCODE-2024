def min_wins_required(X, Y):
    # Points needed to qualify
    points_needed = X
    
    # Maximum points from all ties
    max_tie_points = Y  # Each tie gives 1 point

    # Points still needed after all possible ties
    remaining_points = points_needed - max_tie_points

    # If remaining_points is less than or equal to 0, no wins are needed
    if remaining_points <= 0:
        return 0
    
    # Minimum wins needed if remaining points are still greater than 0
    # Each win gives 2 points, so we need ceiling of remaining_points / 2
    min_wins = (remaining_points + 1) // 2

    return min_wins

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        X, Y = map(int, input("Enter the required points and remaining matches (X Y): ").split())
        results.append(min_wins_required(X, Y))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
