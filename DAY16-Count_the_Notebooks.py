def count_notebooks(N):
    return N * 10

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the weight of the pulp in kgs: "))
        results.append(count_notebooks(N))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
