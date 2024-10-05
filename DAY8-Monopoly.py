def is_monopoly(P, Q, R, S):
    if(P > Q + R + S) or (Q > P + R + S) or (R > P + Q + S) or (S > P + Q + R):
        return "YES"
    else:
        return "NO"

def main():
    T = int(input("enter the test cases(1-5000): "))
    if not (1 <= T <= 5000):
        raise ValueError("The number of test cases must be between 1 and 5000.")
    
    results = []

    for _ in range(T):
        P, Q, R, S = map(int, input("enter the value of P,Q,R,S(1-100) seperated by space: ").split())
        if not (1 <= P <= 100) or not (1 <= Q <= 100) or not (1 <= R <= 100) or not (1 <= S <= 100):
            raise ValueError("Profits must be between 1 and 100.")
        
        results.append(is_monopoly(P, Q, R, S))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
