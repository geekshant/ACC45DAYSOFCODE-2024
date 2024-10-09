def determine_nationality(gestures):
    if 'I' in gestures:
        return "INDIAN"
    elif 'Y' in gestures:
        return "NOT INDIAN"
    else:
        return "NOT SURE"

def main():
    T = int(input("Enter the number of people observed (1-1000): "))
    if not (1 <= T <= 1000):
        raise ValueError("The number of test cases must be between 1 and 1000.")
    
    results = []

    for _ in range(T):
        N = int(input("Enter the number of gestures for this person (1-1000): "))
        if not (1 <= N <= 1000):
            raise ValueError("The number of gestures must be between 1 and 1000.")
        
        gestures = input("Enter the gestures: ").strip()
        if len(gestures) != N:
            raise ValueError("The length of gestures must equal N.")
        
        results.append(determine_nationality(gestures))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
