def does_chef_qualify(X, A, B):
    total_points = A * 1 + B * 2
    return "Qualify" if total_points >= X else "NotQualify"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        X, A, B = map(int, input("Enter X, A, and B separated by spaces: ").split())
        results.append(does_chef_qualify(X, A, B))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
