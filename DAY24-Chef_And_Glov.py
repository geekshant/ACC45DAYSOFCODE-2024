def check_glove_orientation(N, L, G):
    front = True
    back = True
    
    for i in range(N):
        if L[i] > G[i]:
            front = False
        if L[i] > G[N - 1 - i]:
            back = False
    
    if front and back:
        return "both"
    elif front:
        return "front"
    elif back:
        return "back"
    else:
        return "none"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of fingers: "))
        L = list(map(int, input("Enter the lengths of the fingers: ").split()))
        G = list(map(int, input("Enter the lengths of the sheaths: ").split()))
        results.append(check_glove_orientation(N, L, G))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
