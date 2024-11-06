def determine_laptop_recommendation(N, recommendations):
    count = [0] * 10
    
    for recommendation in recommendations:
        count[recommendation - 1] += 1

    max_recommendations = max(count)
    max_recommended_laptops = [i + 1 for i in range(10) if count[i] == max_recommendations]

    if len(max_recommended_laptops) > 1:
        return "CONFUSED"
    else:
        return str(max_recommended_laptops[0])

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of Chef's friends: "))
        recommendations = list(map(int, input("Enter the recommendations separated by spaces: ").split()))
        results.append(determine_laptop_recommendation(N, recommendations))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
