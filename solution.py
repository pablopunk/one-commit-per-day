
cache = {} # we use a dictionary to save calculated Fibonacci values (so we don't calculate them again and again)
# cache.get(x, y) returns a value for the given key 'x'. If key is not available, then returns default value 'y'

def fib(num):
    if num < 2:
        cache[num] = num
    else:
        # it gets the number from the cache if we already calculated it (get() doesn't return 0)
        cache[num] = cache.get(num, 0) or (fib(num-1) + fib(num-2))

    return cache[num]

def solution(maxfib = 10):
    sum = 0; i = 2; current = 0
    while current < maxfib:
        current = fib(i)
        if current % 2 == 0: sum += current
        i += 1
    return sum

if __name__ == "__main__":
    print "The final sum is", solution(4000000)
