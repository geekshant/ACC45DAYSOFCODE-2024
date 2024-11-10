def minimum_time(N, X, health_points):
    # Calculate the time for Single-Target Mode
    single_target_time = sum((h + X - 1) // X for h in health_points)
    
    # Calculate the time for Multi-Target Mode
    max_health = max(health_points)
    multi_target_time = max_health
    
    # Return the minimum of both times
    return min(single_target_time, multi_target_time)

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, X = map(int, input().split())
        health_points = list(map(int, input().split()))
        results.append(minimum_time(N, X, health_points))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
