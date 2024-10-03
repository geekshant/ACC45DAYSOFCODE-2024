def max_points(X, Y):
    # Points if Chef solves problem A first
    points_A_first = max(0, 500 - 2 * X) + max(0, 1000 - 4 * (X + Y))
    # Points if Chef solves problem B first
    points_B_first = max(0, 1000 - 4 * Y) + max(0, 500 - 2 * (X + Y))
    # Return the maximum points possible
    return max(points_A_first, points_B_first)

def main():
    T = int(input("Enter the number of test cases (1-1000): "))
    if not (1 <= T <= 1000):
        raise ValueError("The number of test cases must be between 1 and 1000.")

    results = []

    for _ in range(T):
        X, Y = map(int, input("Enter X and Y separated by a space (1-100): ").split())
        if not (1 <= X <= 100) or not (1 <= Y <= 100):
            raise ValueError("X and Y must be between 1 and 100.")
        results.append(max_points(X, Y))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
