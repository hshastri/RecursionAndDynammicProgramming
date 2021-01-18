def countPathsRecurNaive(numOfStairs):
    if numOfStairs == 0:
        return 1
    if numOfStairs < 0:
        return 0
    else:
        return countPathsRecurNaive(numOfStairs - 1) + countPathsRecurNaive(numOfStairs - 2) + countPathsRecurNaive(numOfStairs - 3)

def countPathsRecurMemo(numOfStairs):
    memo = [-1 for i in range(numOfStairs + 1)]
    return countPathsRecurMemoHelper(numOfStairs, memo)

def countPathsRecurMemoHelper(numOfStairs, memo):

    if numOfStairs == 0:
        return 1
    if numOfStairs < 0:
        return 0

    if memo[numOfStairs] != -1:
        return memo[numOfStairs]

    else:
        memo[numOfStairs] = countPathsRecurMemoHelper(numOfStairs - 1, memo) + countPathsRecurMemoHelper(numOfStairs - 2, memo) + countPathsRecurMemoHelper(numOfStairs - 3, memo)
    return memo[numOfStairs]

def countPathsDynamic(numOfStairs):
    paths = [1, 1, 2] #stay put for path[0]; one leap for path[1]; path[2] = path[0] + path[1]

    for i in range(3, numOfStairs + 1):
        paths.append(paths[i - 1] + paths[i - 2] + paths[i - 3])

    return paths[numOfStairs]

def countPathsDynamicSpaceOptimized(numOfStairs):
    paths = [1, 1, 2]  # stay put for path[0]; one leap for path[1]; path[2] = path[0] + path[1]

    ways = 0
    for i in range(3, numOfStairs + 1):
        ways = paths[2] + paths[1] + paths[0]
        paths[0] = paths[1]
        paths[1] = paths[2]
        paths[2] = ways

    return ways


def main():

    numberOfStairs = 10
    paths = countPathsDynamic(numberOfStairs)
    pathsR = countPathsRecurNaive(numberOfStairs)
    pathsRM = countPathsRecurMemo(numberOfStairs)
    pathsSpace = countPathsDynamicSpaceOptimized(numberOfStairs)
    print(paths)
    print(pathsR)
    print(pathsRM)
    print(pathsSpace)
    
if __name__ == '__main__':
    main()