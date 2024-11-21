def find_missing_doll_type(dolls):
    from collections import defaultdict
    
    doll_count = defaultdict(int)
    
    for doll in dolls:
        doll_count[doll] += 1
    
    for doll, count in doll_count.items():
        if count % 2 != 0:
            return doll

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        N = int(input("Enter the number of dolls: "))
        dolls = [int(input()) for _ in range(N)]
        results.append(find_missing_doll_type(dolls))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
