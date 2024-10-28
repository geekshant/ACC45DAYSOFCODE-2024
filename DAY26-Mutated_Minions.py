def mutated_minions(T, test_cases):
    results = []
    
    for test_case in test_cases:
        N, K = test_case[0]
        characteristics = test_case[1]
        
        wolverine_count = 0
        for characteristic in characteristics:
            if (characteristic + K) % 7 == 0:
                wolverine_count += 1
                
        results.append(wolverine_count)
    
    return results

def main():
    T = int(input("Enter the number of test cases: "))
    test_cases = []

    for _ in range(T):
        N, K = map(int, input("Enter the values of N and K separated by spaces: ").split())
        characteristics = list(map(int, input("Enter the initial characteristic values of the minions separated by spaces: ").split()))
        test_cases.append(((N, K), characteristics))

    results = mutated_minions(T, test_cases)

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
