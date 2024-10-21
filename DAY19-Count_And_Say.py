def count_and_say(n):
    if n == 1:
        return "1"
    
    previous_term = count_and_say(n - 1)
    result = ""
    count = 1
    for i in range(1, len(previous_term)):
        if previous_term[i] == previous_term[i - 1]:
            count += 1
        else:
            result += str(count) + previous_term[i - 1]
            count = 1
    result += str(count) + previous_term[-1]
    
    return result

def main():
    # Take input from the user
    n = int(input("Enter a positive integer n: "))
    
    # Generate the nth element of the count-and-say sequence
    result = count_and_say(n)
    
    print(f"The {n}th element of the count-and-say sequence is: {result}")

if __name__ == "__main__":
    main()
