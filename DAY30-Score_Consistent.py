def is_possible(A, B, C, D):
    if A <= C and B <= D:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        A, B = map(int, input("Enter the initial scores of team 1 and team 2 separated by spaces: ").split())
        C, D = map(int, input("Enter the desired scores of team 1 and team 2 separated by spaces: ").split())
        results.append(is_possible(A, B, C, D))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
