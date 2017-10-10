def measure_time(f, n):
    import time
    start_time = time.time()
    res = f(n)
    end_time = time.time()
    return end_time-start_time, res

def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    import time, sys
    time, fib = measure_time(fibonacci, int(sys.argv[1]))
    print("{} ({})".format(fib, time))

if __name__=='__main__':
    main()
