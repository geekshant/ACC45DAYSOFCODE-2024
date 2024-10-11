def max_houses_destroyed(N, X, defense):
    destroyed = 0
    for i in range(N):
        if defense[i] < X:
            destroyed = i + 1
    return destroyed

def main():
    T = int(input("Enter the number of test cases (1-100): "))
    if not (1 <= T <= 100):
        raise ValueError("The number of test cases must be between 1 and 100.")
    
    results = []

    for _ in range(T):
        N, X = map(int, input("Enter the values of N and X separated by a space: ").split())
        if not (1 <= N <= 100000) or not (1 <= X <= 1000000000):
            raise ValueError("Values must satisfy 1 ≤ N ≤ 100,000 and 1 ≤ X ≤ 1,000,000,000.")
        
        defense = list(map(int, input("Enter the defense values separated by spaces: ").split()))
        if len(defense) != N or any(not (1 <= a <= 1000000000) for a in defense):
            raise ValueError("Each defense value must be between 1 and 1,000,000,000, and the length of the list must be N.")
        
        results.append(max_houses_destroyed(N, X, defense))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
