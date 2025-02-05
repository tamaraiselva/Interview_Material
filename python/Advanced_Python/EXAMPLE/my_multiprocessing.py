import multiprocessing

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find primes in a given range
def find_primes_in_range(start, end):
    return [n for n in range(start, end) if is_prime(n)]

# Function to divide work across multiple processes
def parallel_prime_finder(n, num_processes=4):
    pool = multiprocessing.Pool(processes=num_processes)
    
    # Split the range into chunks based on the number of processes
    chunk_size = n // num_processes
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)]
    
    # Find primes in parallel
    results = pool.starmap(find_primes_in_range, ranges)
    pool.close()
    pool.join()
    
    # Flatten results
    primes = [prime for sublist in results for prime in sublist]
    return primes

if __name__ == "__main__":
    n = 100000  # Range up to 100,000
    num_processes = 4  # Number of processes to use
    
    primes = parallel_prime_finder(n, num_processes)
    print(f"Found {len(primes)} prime numbers.")
