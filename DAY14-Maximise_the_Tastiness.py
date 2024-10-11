def max_tastiness(a, b, c, d):
    return max(a + c, a + d, b + c, b + d)

def main():
    T = int(input("Enter the number of test cases: "))
    if not (1 <= T <= 100):
        raise ValueError("The number of test cases must be between 1 and 100.")
    
    results = []

    for _ in range(T):
        a, b, c, d = map(int, input("Enter the tastiness of four ingredients separated by spaces: ").split())
        if not (1 <= a <= 100) or not (1 <= b <= 100) or not (1 <= c <= 100) or not (1 <= d <= 100):
            raise ValueError("Each tastiness value must be between 1 and 100.")
        
        results.append(max_tastiness(a, b, c, d))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
