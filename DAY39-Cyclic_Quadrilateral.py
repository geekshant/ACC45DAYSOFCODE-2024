def is_cyclic_quadrilateral(A, B, C, D):
    # Check if the sum of opposite angles is 180 degrees
    if (A + C == 180 and B + D == 180):
        return "YES"
    else:
        return "NO"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        A, B, C, D = map(int, input("Enter the four angles separated by spaces: ").split())
        results.append(is_cyclic_quadrilateral(A, B, C, D))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
