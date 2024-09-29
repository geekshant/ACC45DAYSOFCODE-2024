def determine_rank(scores_dragon, scores_sloth):
    total_dragon = sum(scores_dragon)
    total_sloth = sum(scores_sloth)
    
    # using nested if-else 
    
    if total_dragon > total_sloth:
        return "Dragon"
    elif total_sloth > total_dragon:
        return "Sloth"
    else:
        if scores_dragon[0] > scores_sloth[0]:
            return "Dragon"
        elif scores_sloth[0] > scores_dragon[0]:
            return "Sloth"
        else:
            if scores_dragon[1] > scores_sloth[1]:
                return "Dragon"
            elif scores_sloth[1] > scores_dragon[1]:
                return "Sloth"
            else:
                return "Tie"

# Input: number of test cases
T = int(input("enter the number of test cases: "))

results = []

# Process each test case
for _ in range(T):
    scores_dragon = list(map(int, input("enter the scores of dragon seperated by space: ").split()))
    scores_sloth = list(map(int, input("enter the scores of sloth seperated by space: ").split()))
    result = determine_rank(scores_dragon, scores_sloth)
    results.append(result)

# Output results for each test case
for result in results:
    print(result)
    
'''

example for instance: if i take T = 1, which is number of test cases 
and give scores to dragon as 50 45 55 and sloth as 40 75 and 35 the output will be dragon

'''
