import math

def minimum_masks_required(N, A):
    return math.ceil(A / 2)

def main():
    T = int(input("Enter the number of test cases (1-100000): ").strip())
    if not (1 <= T <= 100000):
        raise ValueError("The number of test cases must be between 1 and 100,000.")
    
    results = []

    for _ in range(T):
        N, A = map(int, input("Enter the value of N and A separated by a space: ").strip().split())
        if not (2 <= N <= 400) or not (1 <= A < N):
            raise ValueError("N must be between 2 and 400, and A must be between 1 and N-1.")
        
        results.append(minimum_masks_required(N, A))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
