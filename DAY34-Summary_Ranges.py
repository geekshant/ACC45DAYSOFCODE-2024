def summary_ranges(nums):
    ranges = []
    if not nums:
        return ranges
    
    start = nums[0]
    end = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            if start == end:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}->{end}")
            start = nums[i]
            end = nums[i]
    
    if start == end:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}->{end}")
    
    return ranges

def main():
    nums = list(map(int, input("Enter the sorted unique integers array separated by spaces: ").split()))
    result = summary_ranges(nums)
    
    print("The smallest sorted list of ranges that cover all the numbers in the array exactly:")
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
