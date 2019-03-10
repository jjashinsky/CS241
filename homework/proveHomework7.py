def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        prev1 = fib(n-1)
        prev2 = fib(n-2)
        sum = prev1 + prev2
        return sum
    

def main():
    fibo = fib(20)
    print("The Fibonacci number is: {}" .format(fibo))
    
    
    for i in range(21):
        fibo = fib(i)
        print("The Fibonacci number is: {}" .format(fibo))

if __name__ == "__main__":
    main()