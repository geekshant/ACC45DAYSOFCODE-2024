def can_a_win_election(N, X, votes_A, votes_B):
    states_needed = (N // 2) + 1  # States needed to win the election (more than half)
    current_wins = sum(1 for i in range(N) if votes_A[i] > votes_B[i])  # Current wins for A

    if current_wins >= states_needed:
        return "YES"

    deficits = []  # List to store the deficit votes needed to flip states in favor of A
    for i in range(N):
        if votes_A[i] <= votes_B[i]:
            deficits.append(votes_B[i] - votes_A[i] + 1)

    # Sort deficits in ascending order to use the minimum votes first
    deficits.sort()

    # Try to flip states using the available X votes
    for deficit in deficits:
        if X >= deficit:
            X -= deficit
            current_wins += 1
            if current_wins >= states_needed:
                return "YES"
        else:
            break

    return "NO"

def main():
    T = int(input("enter the number of test cases: ").strip())
    results = []

    for _ in range(T):
        N, X = map(int, input("enter the value of N and X seperated by space: ").strip().split())
        votes_A = list(map(int, input("enter the value of votes A: ").strip().split()))
        votes_B = list(map(int, input("enter the value of votes B: ").strip().split()))
        results.append(can_a_win_election(N, X, votes_A, votes_B))

    print("\n".join(results))

if __name__ == "__main__":
    main()
