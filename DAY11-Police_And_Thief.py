def minimum_time_to_catch_thief(X, Y):
    # Calculate the absolute distance between the policeman and the thief
    distance = abs(X - Y)
    # The relative speed of catching up is 1 unit per second (2 - 1 = 1)
    time_to_catch = distance // 1
    return time_to_catch

def main():
    T = int(input("Enter the number of test cases (1-1000): ").strip())
    if not (1 <= T <= 1000):
        raise ValueError("The number of test cases must be between 1 and 1000.")
    
    results = []

    for _ in range(T):
        X, Y = map(int, input("Enter the values of X and Y separated by a space: ").strip().split())
        if not (-10**5 <= X <= 10**5) or not (-10**5 <= Y <= 10**5):
            raise ValueError("X and Y must be between -100,000 and 100,000.")
        
        results.append(minimum_time_to_catch_thief(X, Y))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
