def select_movie(n, lengths, ratings):
    max_value = -1
    selected_index = -1
    
    for i in range(n):
        product = lengths[i] * ratings[i]
        if product > max_value or (product == max_value and ratings[i] > ratings[selected_index]):
            max_value = product
            selected_index = i
        elif product == max_value and ratings[i] == ratings[selected_index] and i < selected_index:
            selected_index = i
    
    return selected_index + 1

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        n = int(input("Enter the number of movies: "))
        lengths = list(map(int, input("Enter the lengths of the movies separated by spaces: ").split()))
        ratings = list(map(int, input("Enter the ratings of the movies separated by spaces: ").split()))
        results.append(select_movie(n, lengths, ratings))
    
    print("\nSelected Movies:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
