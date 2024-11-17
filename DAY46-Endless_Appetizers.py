import math

def max_plates(X, Y, R):
    extra_sticks = R // 30
    total_sticks = X + extra_sticks
    plates = math.ceil(total_sticks / Y)
    return plates

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        X, Y, R = map(int, input().split())
        results.append(max_plates(X, Y, R))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
