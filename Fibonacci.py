#simple recursion
def FibonacciNaive(n):

    if n < 2:
        return n
    else:
        return FibonacciNaive(n - 1) + FibonacciNaive(n - 2)



#Dynamic Programming: Bottom Up Approach
def FibonacciBottomUp():
    pass

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


if __name__ == '__main__':
    main()