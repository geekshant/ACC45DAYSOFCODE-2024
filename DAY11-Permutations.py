from itertools import permutations

def all_permutations(nums):
    return list(permutations(nums))

if __name__ == "__main__":
    # Take input from the user
    nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    
    # Generate all permutations
    result = all_permutations(nums)
    
    # Print all permutations
    print("\nAll possible permutations:")
    for perm in result:
        print(perm)
