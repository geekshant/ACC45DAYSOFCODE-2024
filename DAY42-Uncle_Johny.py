def find_uncle_johny_position(N, songs, K):
    uncle_johny_length = songs[K - 1]  # Get the length of "Uncle Johny"
    sorted_songs = sorted(songs)  # Sort the playlist
    return sorted_songs.index(uncle_johny_length) + 1  # Return the 1-indexed position

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input())
        songs = list(map(int, input().split()))
        K = int(input())
        results.append(find_uncle_johny_position(N, songs, K))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
