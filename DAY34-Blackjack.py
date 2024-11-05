def find_third_number(A, B):
    required_sum = 21
    C = required_sum - (A + B)
    if 1 <= C <= 10:
        return C
    else:
        return -1

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        A, B = map(int, input("Enter the first and second numbers separated by a space: ").split())
        results.append(find_third_number(A, B))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
