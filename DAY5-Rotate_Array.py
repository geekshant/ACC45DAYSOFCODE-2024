def rotate(nums, k):
    # Ensure k is within the bounds of the array length
    k = k % len(nums)
    # Rotate the array by slicing
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    k = int(input("Enter the value of k: "))
    
print(rotate(nums, k))
