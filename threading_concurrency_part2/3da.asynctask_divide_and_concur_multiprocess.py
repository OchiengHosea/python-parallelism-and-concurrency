"""recursively sum a range of numbers"""
from asyncio import futures
from concurrent.futures import ProcessPoolExecutor, as_completed

def recursive_sum(lo, hi, pool=None):
    if not pool:
        with ProcessPoolExecutor() as executor:
            futures = recursive_sum(lo, hi, pool=executor)
            return sum(f.result() for f in as_completed(futures))
    else:
        if hi - lo <= 100_000:
            return [pool.submit(sum, range(lo, hi))]
        else:
            mid = (hi + lo) // 2
            left = recursive_sum(lo, mid, pool=pool)
            right = recursive_sum(mid, hi, pool=pool)
            return left + right
    
if __name__ == '__main__':
    total = recursive_sum(1, 1_000_000)
    print("total sum is", total)
    