def can_form_groups(N, P):
    from collections import Counter
    count = Counter(P)
    for size, num_people in count.items():
        if num_people % size != 0:
            return "NO"
    return "YES"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of people at the party: "))
        P = list(map(int, input("Enter the preferred group sizes separated by spaces: ").split()))
        results.append(can_form_groups(N, P))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
