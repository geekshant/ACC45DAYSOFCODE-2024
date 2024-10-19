def find_winner(A, B):
    turn = 1
    while True:
        if turn % 2 != 0:  # Limak's turn (odd turns)
            if A >= turn:
                A -= turn
            else:
                return "Bob"
        else:  # Bob's turn (even turns)
            if B >= turn:
                B -= turn
            else:
                return "Limak"
        turn += 1

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        A, B = map(int, input("Enter the values of A and B separated by a space: ").split())
        results.append(find_winner(A, B))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
