def max_tastiness(a, b, c, d):
    return max(a + c, a + d, b + c, b + d)

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        a, b, c, d = map(int, input("Enter the tastiness of four ingredients separated by spaces: ").split())
        results.append(max_tastiness(a, b, c, d))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
