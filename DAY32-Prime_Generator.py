import math

def sieve(limit):
    # Basic sieve to find all primes up to √n
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return primes

def segmented_sieve(m, n, primes):
    # Array for marking non-primes in the range [m, n]
    is_prime_range = [True] * (n - m + 1)
    if m == 1:
        is_prime_range[0] = False  # 1 is not a prime number
    
    # Use primes from basic sieve to mark non-primes in the range [m, n]
    for prime in primes:
        # Find the smallest multiple of prime >= m
        start = max(prime * prime, m + (prime - m % prime) % prime)
        for j in range(start, n + 1, prime):
            is_prime_range[j - m] = False
    
    # Collect all primes in range [m, n]
    result = []
    for i in range(n - m + 1):
        if is_prime_range[i]:
            result.append(m + i)
    return result

def find_primes_in_ranges(test_cases):
    results = []
    max_n = max(n for _, n in test_cases)
    sqrt_max_n = int(math.sqrt(max_n)) + 1
    primes = sieve(sqrt_max_n)  # Primes up to √max(n)
    
    for m, n in test_cases:
        primes_in_range = segmented_sieve(m, n, primes)
        results.append(primes_in_range)
    
    return results

# Reading input
t = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Find primes for each test case
results = find_primes_in_ranges(test_cases)

# Output results
for i, primes in enumerate(results):
    if i > 0:
        print()  # Blank line between test cases
    print("\n".join(map(str, primes)))
