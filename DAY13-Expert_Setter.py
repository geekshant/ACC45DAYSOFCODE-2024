def is_expert(X, Y):
    return "YES" if Y >= X / 2 else "NO"

def main():
    T = int(input("Enter the number of test cases (1-1000): "))
    if not (1 <= T <= 1000):
        raise ValueError("The number of test cases must be between 1 and 1000.")
    
    results = []

    for _ in range(T):
        X, Y = map(int, input("Enter the values of X and Y separated by a space: ").split())
        if not (1 <= Y <= X <= 1000000):
            raise ValueError("Values must satisfy 1 <= Y <= X <= 1,000,000.")
        
        results.append(is_expert(X, Y))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
