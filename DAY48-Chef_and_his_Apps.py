def min_apps_to_delete(S, X, Y, Z):
    # Case 1: Check if the new app can be installed without deleting any apps
    if S - (X + Y) >= Z:
        return 0
    # Case 2: Check if deleting one of the apps makes enough space
    elif S - Y >= Z or S - X >= Z:
        return 1
    # Case 3: If neither of the above is sufficient, both apps must be deleted
    else:
        return 2

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        S, X, Y, Z = map(int, input().split())
        results.append(min_apps_to_delete(S, X, Y, Z))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
