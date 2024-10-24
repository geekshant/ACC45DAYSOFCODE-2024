def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            backtrack(i, target - candidates[i], path + [candidates[i]])

    candidates.sort()
    result = []
    backtrack(0, target, [])
    return result

def main():
    # Take input from the user
    candidates = list(map(int, input("Enter the distinct integers separated by spaces: ").split()))
    target = int(input("Enter the target integer: "))
    
    # Find all unique combinations that sum to target
    result = combination_sum(candidates, target)
    
    print(f"All unique combinations of {candidates} that sum to {target} are:")
    for combo in result:
        print(combo)

if __name__ == "__main__":
    main()
