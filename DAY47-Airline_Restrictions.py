def can_take_all_bags(A, B, C, D, E):
    # Check all combinations of bags
    if (A + B <= D and C <= E) or (A + C <= D and B <= E) or (B + C <= D and A <= E):
        return "YES"
    else:
        return "NO"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        A, B, C, D, E = map(int, input().split())
        results.append(can_take_all_bags(A, B, C, D, E))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
