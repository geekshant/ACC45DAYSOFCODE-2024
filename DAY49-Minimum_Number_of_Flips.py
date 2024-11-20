def min_operations_to_zero_sum(N, A):
    total_sum = sum(A)
    
    # If the sum is already 0
    if total_sum == 0:
        return 0
    
    # If the absolute value of sum is odd, it's impossible to make it zero
    if abs(total_sum) % 2 != 0:
        return -1
    
    # Calculate the minimum number of operations needed
    # We need half of the absolute sum to be changed to zero out the total sum
    required_change = abs(total_sum) // 2
    
    count_1 = A.count(1)
    count_minus_1 = A.count(-1)
    
    # Check if it's possible to change the sum
    if required_change <= count_1 or required_change <= count_minus_1:
        return required_change
    else:
        return -1

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        results.append(min_operations_to_zero_sum(N, A))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
