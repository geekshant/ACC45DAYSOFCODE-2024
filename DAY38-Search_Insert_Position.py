def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

def main():
    nums = list(map(int, input("Enter the sorted array of distinct integers separated by spaces: ").split()))
    target = int(input("Enter the target value: "))
    
    index = search_insert_position(nums, target)
    
    print(f"The index of the target value is: {index}")

if __name__ == "__main__":
    main()
