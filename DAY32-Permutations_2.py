from itertools import permutations

def unique_permutations(nums):
    # Use a set to store unique permutations
    perms = set(permutations(nums))
    return [list(perm) for perm in perms]

def main():
    nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    result = unique_permutations(nums)
    
    print("All possible unique permutations are:")
    for perm in result:
        print(perm)

if __name__ == "__main__":
    main()
