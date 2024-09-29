def removeDuplicates(nums):
    if not nums:
        return 0
    
    # Pointer for the place of the next unique element
    k = 1
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
            
    return k

# Example usage
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k1 = removeDuplicates(nums1)
k2 = removeDuplicates(nums2)

# k1: is number of unique elements in the num1 array after removing duplicates
# k2: is number of unique elements in the num2 array after removing duplicates

print(k1, nums1[:k1])  # Output: 2, [1, 2]
print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]
