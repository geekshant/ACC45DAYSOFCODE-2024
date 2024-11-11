from collections import Counter
import heapq

def k_most_frequent_elements(nums, k):
    # Count the frequency of each element in nums
    frequency = Counter(nums)
    
    # Use a heap to get the k most frequent elements
    most_frequent = heapq.nlargest(k, frequency.keys(), key=frequency.get)
    
    return most_frequent

def main():
    nums = list(map(int, input("Enter the integer array separated by spaces: ").split()))
    k = int(input("Enter the value of k: "))
    
    result = k_most_frequent_elements(nums, k)
    
    print("The", k, "most frequent elements are:", result)

if __name__ == "__main__":
    main()
