import decimal
from concurrent.futures import ProcessPoolExecutor

# Set decimal precision
decimal.getcontext().prec = 100000000

def calculate_term(i):
    """Calculate the i-th term"""
    return decimal.Decimal((-1) ** i) * (decimal.Decimal(4) / (decimal.Decimal(2 * i + 1)))

def calculate_pi_chunk(start, end):
    """Calculate terms within the given range"""
    total = decimal.Decimal(0)
    for i in range(start, end):
        total += calculate_term(i)
    return total

def calculate_pi_parallel(num_terms, num_workers):
    """Calculate π in parallel"""
    chunk_size = num_terms // num_workers
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Distribute work among processes for parallel execution
        futures = [executor.submit(calculate_pi_chunk, i * chunk_size, (i + 1) * chunk_size) for i in range(num_workers)]
        
        # Sum up the results from parallel calculations
        pi = sum(f.result() for f in futures)
    
    return pi

if __name__ == "__main__":
    num_terms = 1000000  # Number of terms to calculate
    num_workers = 8      # Number of processes to use (set according to CPU cores)

    pi_approx = calculate_pi_parallel(num_terms, num_workers)
    print(f"Calculated value of π: {pi_approx}")
