def generate_parentheses(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack()
    return result

def main():
    # Take input from the user
    n = int(input("Enter the number of pairs of parentheses: "))
    
    # Generate the combinations of well-formed parentheses
    result = generate_parentheses(n)
    
    print(f"All combinations of well-formed parentheses with {n} pairs are:")
    for combo in result:
        print(combo)

if __name__ == "__main__":
    main()
