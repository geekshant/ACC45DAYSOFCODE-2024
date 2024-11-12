def max_people_can_bathe(X, Y):
    # Each person requires 2 buckets of water
    water_needed_per_person = 2 * Y
    return X // water_needed_per_person

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        X, Y = map(int, input().split())
        results.append(max_people_can_bathe(X, Y))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
