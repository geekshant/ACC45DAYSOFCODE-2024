def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

def main():
    nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    val = int(input("Enter the value to remove: "))
    
    k = remove_element(nums, val)
    
    print(f"Array after removal: {nums[:k]}")
    print(f"Number of elements not equal to {val}: {k}")

if __name__ == "__main__":
    main()
