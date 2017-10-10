def measure_time(f, n):
    import time
    start_time = time.time()
    res = f(n)
    end_time = time.time()
    return end_time-start_time, res

memorised_fibonacci = {}
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        if n not in memorised_fibonacci:
            memorised_fibonacci[n] = fibonacci(n-1) + fibonacci(n-2)
        return memorised_fibonacci[n]

def main():
    import time, sys
    time, fib = measure_time(fibonacci, int(sys.argv[1]))
    print("{} ({})".format(fib, time))

if __name__=='__main__':
    main()
