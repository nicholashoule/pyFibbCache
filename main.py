import time
# from functools import lru_cache


# f: fibb
def fibb(n):
    '''fibb
    params: Index n
    return: A fibbonacci value for a given index
    '''
    # Check the cache for n
    if n in cache:
        return cache[n]

    if (n == 0):
        result = 0
    elif (n == 1):
        result = 1
    else:
        result = fibb(n - 1) + fibb(n - 2)

    # Cache values to speed up calculation time
    cache[n] = result
    return result


# f: main
def main():
    '''main
    program driver
    '''
    for i in range(43):
        print(f"{i}: {fibb(i)}")


# Recursive Method with implicit cache provided by functools
# ... https://docs.python.org/3/library/functools.html#functools.lru_cache
# Decorator to wrap a function with a memoizing callable that saves up to
# the maxsize most recent calls. It can save time when an expensive
# or I/O bound function is periodically called with the same arguments.
# set cache with 1000
# @lru_cache(maxsize = 1000)

# Using explicit cache
cache = {}

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time: {end - start}")
