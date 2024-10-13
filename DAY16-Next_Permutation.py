def next_permutation(nums):
    n = len(nums)
    
    # Step 1: Find the first decreasing element
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:  # If the array is not entirely in descending order
        # Step 2: Find the element that is just larger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap elements
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the right part
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def main():
    nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    next_permutation(nums)
    print("The next permutation is:", nums)

if __name__ == "__main__":
    main()
