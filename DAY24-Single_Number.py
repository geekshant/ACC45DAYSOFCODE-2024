def find_single_number(nums):
    single_number = 0
    for num in nums:
        single_number ^= num
    return single_number

def main():
    # Take input from the user
    nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    
    # Find the single number
    result = find_single_number(nums)
    
    print(f"The single number in the array is: {result}")

if __name__ == "__main__":
    main()
