def predict_winner(N):
    if N % 3 == 0:
        return "BOB"
    else:
        return "ALICE"

def main():
    T = int(input("Enter the number of test cases (1-10): "))
    if not (1 <= T <= 10):
        raise ValueError("The number of test cases must be between 1 and 10.")
    
    results = []

    for _ in range(T):
        N = int(input("Enter the limit N (1-10): "))
        if not (1 <= N <= 10):
            raise ValueError("N must be between 1 and 10.")
        
        results.append(predict_winner(N))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
