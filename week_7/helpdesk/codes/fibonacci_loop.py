def measure_time(f, n):
    import time
    start_time = time.time()
    res = f(n)
    end_time = time.time()
    return end_time-start_time, res

def fibonacci(n):
    a0 = 0
    a1 = 1
    a2 = 1
    for i in range(n-1):
        a2 = a0+a1
        a0 = a1
        a1 = a2
    return a2

def main():
    import time, sys
    time, fib = measure_time(fibonacci, int(sys.argv[1]))
    print("{} ({})".format(fib, time))

if __name__=='__main__':
    main()
