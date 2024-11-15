def max_people_in_office(swipes):
    current_people = 0
    max_people = 0
    swipe_count = {}

    for swipe in swipes:
        if swipe in swipe_count:
            swipe_count[swipe] += 1
        else:
            swipe_count[swipe] = 1

        # If the count is odd, it means the person is entering
        if swipe_count[swipe] % 2 == 1:
            current_people += 1
        else:
            current_people -= 1

        # Update the maximum number of people in the office
        if current_people > max_people:
            max_people = current_people

    return max_people

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input())
        swipes = list(map(int, input().split()))
        results.append(max_people_in_office(swipes))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
