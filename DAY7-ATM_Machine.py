def atm_withdrawals(N, K, A):
    result = []
    for amount in A:
        if K >= amount:
            result.append('1')
            K -= amount
        else:
            result.append('0')
    return ''.join(result)

def main():
    T = int(input("Enter the number of test cases (1-100): "))
    if not (1 <= T <= 100):
        raise ValueError("The number of test cases must be between 1 and 100.")
    
    results = []

    for _ in range(T):
        N, K = map(int, input("Enter N and K separated by a space: ").split())
        if not (1 <= N <= 100) or not (1 <= K <= 1_000_000):
            raise ValueError("N must be between 1 and 100, and K must be between 1 and 1,000,000.")
        
        A = list(map(int, input(f"Enter {N} space-separated integers for A (each between 1 and 1,000,000): ").split()))
        if len(A) != N or any(not (1 <= amount <= 1_000_000) for amount in A):
            raise ValueError("Each element of A must be between 1 and 1,000,000, and the length of A must be N.")
        
        results.append(atm_withdrawals(N, K, A))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
