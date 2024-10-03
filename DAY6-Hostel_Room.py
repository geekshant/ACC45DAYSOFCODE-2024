def max_people_in_room(N, X, A):
    current_people = X
    max_people = X
    
    for people in A:
        current_people += people
        if current_people > max_people:
            max_people = current_people
            
    return max_people

def main():
    T = int(input("Enter the number of test cases (1-100): "))
    if not (1 <= T <= 100):
        raise ValueError("Number of test cases must be between 1 and 100.")
    
    results = []
    
    for _ in range(T):
        N, X = map(int, input("Enter N and X separated by a space (N: 1-100, X: 0-100): ").split())
        if not (1 <= N <= 100) or not (0 <= X <= 100):
            raise ValueError("N must be between 1 and 100, and X must be between 0 and 100.")
        
        A = list(map(int, input(f"Enter {N} space-separated integers for A (each between -100 and 100): ").split()))
        if len(A) != N or any(not (-100 <= ai <= 100) for ai in A):
            raise ValueError("Each element of A must be between -100 and 100, and the length of A must be N.")
        
        results.append(max_people_in_room(N, X, A))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
