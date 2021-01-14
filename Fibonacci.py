#simple recursion
def FibonacciNaive(n):

    if n < 2:
        return n
    else:
        return FibonacciNaive(n - 1) + FibonacciNaive(n - 2)

#Dynamic Programming: Bottom Up Approach
def FibonacciBottomUp(n):
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n]

#Dynamic Programming: Memoized solution
def FibonacciMemoized(n):
  memoize = [None for x in range(n+1)]
  return FibonacciRecurMemoized(memoize, n)


def FibonacciRecurMemoized(memoize, n):
  if n < 2:
    return n

  # if we have already solved this subproblem, simply return the result from the cache
  elif memoize[n] != None:
    return memoize[n]

  else:
      memoize[n] = FibonacciRecurMemoized(memoize, n - 1) + FibonacciRecurMemoized(memoize, n - 2)
      return memoize[n]

def main():
    print(FibonacciNaive(30))
    print(FibonacciMemoized(100)) #works substantially faster for larger inputs
    print(FibonacciBottomUp(100)) #more expeditious performance than naive recursion

    print(FibonacciMemoized(4))

if __name__ == '__main__':
    main()