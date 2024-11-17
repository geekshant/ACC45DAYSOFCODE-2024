import math

def minimum_time_single_target(healths, X):
    time = 0
    for health in healths:
        time += math.ceil(health / X)
    return time

def minimum_time_multi_target(healths):
    return max(healths)

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        N, X = map(int, input().split())
        healths = list(map(int, input().split()))
        
        time_single_target = minimum_time_single_target(healths, X)
        time_multi_target = minimum_time_multi_target(healths)
        
        results.append(min(time_single_target, time_multi_target))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
