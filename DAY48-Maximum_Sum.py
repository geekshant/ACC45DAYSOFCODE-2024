def max_subarray_sum(nums, k):
    n = len(nums)
    if k > n:
        return 0
    
    max_sum = 0
    for i in range(n - k + 1):
        subarray = nums[i:i+k]
        if len(set(subarray)) == k:
            current_sum = sum(subarray)
            max_sum = max(max_sum, current_sum)
    
    return max_sum

def main():
    nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    k = int(input("Enter the value of k: "))
    result = max_subarray_sum(nums, k)
    print(result)

if __name__ == "__main__":
    main()
