def encode_dna(N, S):
    # Dictionary to map binary pairs to DNA characters
    encoding = {
        '00': 'A',
        '01': 'T',
        '10': 'C',
        '11': 'G'
    }
    result = []
    
    # Iterate through the binary string in pairs
    for i in range(0, N, 2):
        pair = S[i:i+2]
        result.append(encoding[pair])
    
    return ''.join(result)

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        N = int(input())
        S = input().strip()
        results.append(encode_dna(N, S))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
