def is_easy_to_pronounce(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consecutive_consonants = 0
    
    for char in s:
        if char in vowels:
            consecutive_consonants = 0  # reset the count on vowel
        else:
            consecutive_consonants += 1  # increase the count on consonant
        
        if consecutive_consonants >= 4:
            return "NO"
    
    return "YES"

# here T is the number of test cases 

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
# N and S are the length of string and the string itself respectively  

    for _ in range(T):
        N = int(input("Enter the length of the string: "))  # Read N
        S = input("Enter the string: ")  # Read the string
        result = is_easy_to_pronounce(S)
        results.append(result)
    
    # Output results
    print("\n".join(results))

if __name__ == "__main__":
    main()

# if i run this code and assign the value of T = 1, N = 9 & S = deekshant the output will be Yes 

'''

Yes: easy to pronounce
No: hard to pronounce

'''