def is_ball_in(r1, r2, r3, r4):
    return "IN" if r1 == 0 and r2 == 0 and r3 == 0 and r4 == 0 else "OUT"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        r1, r2, r3, r4 = map(int, input("Enter the decisions of the 4 referees separated by spaces: ").split())
        results.append(is_ball_in(r1, r2, r3, r4))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
