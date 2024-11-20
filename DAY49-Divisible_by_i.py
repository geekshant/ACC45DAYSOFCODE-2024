def construct_permutation(N):
    return list(range(N, 0, -1))

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        N = int(input())
        permutation = construct_permutation(N)
        results.append(permutation)
    
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
