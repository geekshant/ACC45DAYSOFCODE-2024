def can_form_array(N, B):
    count_ones = B.count(1)
    if count_ones % 2 == 0:
        return "YES"
    else:
        return "NO"

def main():
    T = int(input("enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("size of Array: "))
        B = list(map(int, input("numbers in array: ").split()))
        results.append(can_form_array(N, B))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
