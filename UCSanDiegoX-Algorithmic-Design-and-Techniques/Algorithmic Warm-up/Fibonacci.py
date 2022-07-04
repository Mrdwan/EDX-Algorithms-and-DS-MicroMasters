# Fibonacci 

results = {
    0: 0,
    1: 1
}

def calc_fib(n):
    if n in results:
        return results[n]

    results[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return results[n]
    

n = int(input())
print(calc_fib(n))