def can_measure_weight(W, X, Y, Z):
    weights = [X, Y, Z]
    for i in range(1 << len(weights)):
        sum_weights = 0
        for j in range(len(weights)):
            if i & (1 << j):
                sum_weights += weights[j]
        if sum_weights == W:
            return "YES"
    return "NO"

def main():
    T = int(input("enter the number of test cases(1-10^4): "))
    if not (1 <= T <= 10**4):
        raise ValueError("The number of test cases must be between 1 and 10,000.")
    
    results = []

    for _ in range(T):
        W, X, Y, Z = map(int, input("enter the value of W,X,Y,Z seperated by space: ").split())
        if not (1 <= W <= 10**5) or not (1 <= X <= 10**5) or not (1 <= Y <= 10**5) or not (1 <= Z <= 10**5):
            raise ValueError("W, X, Y, and Z must be between 1 and 100,000.")
        
        results.append(can_measure_weight(W, X, Y, Z))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
