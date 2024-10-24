def degree_of_polynomial(N, coefficients):
    # Find the highest index with a non-zero coefficient
    degree = N - 1  # Start with the highest index
    while degree >= 0 and coefficients[degree] == 0:
        degree -= 1
    return degree

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of terms in the polynomial: "))
        coefficients = list(map(int, input("Enter the coefficients separated by spaces: ").split()))
        results.append(degree_of_polynomial(N, coefficients))

    print("\nDegrees of the polynomials:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
