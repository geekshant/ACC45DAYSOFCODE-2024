def calculate_watching_time(X, Y):
    if Y % 2 != 0:
        return "Y should be even."
    
    time_spent = (Y // 2) + (X - Y)
    return time_spent

def main():
    X, Y = map(int, input("Enter X and Y separated by spaces: ").split())
    result = calculate_watching_time(X, Y)
    print("Total time Chef spends watching the movie:", result)

if __name__ == "__main__":
    main()
