#Dynamic Programming
def MakeChange(arr, val):

    #2d array storing number of ways
    ways = [[0 for col in range(0, val + 1)] for row in range(0, len(arr) + 1)]

    #number of ways to make change for 0 is 1, pick nothing
    for row in range(len(arr) + 1):
        ways[row][0] = 1

    for row in range(1, len(arr) + 1):
        for col in range(1, val + 1):
            #if the cpin value is larger than the ampount remaining, then
            if arr[row - 1] > col:
                ways[row][col] = ways[row - 1][col]
            else:
                ways[row][col] = ways[row - 1][col] + ways[row][col - arr[row - 1]]

    return ways[len(arr)][val]


def main():
    arrOfCoins = [1, 3, 4]
    val = 7
    print(MakeChange(arrOfCoins, val))

if __name__ == '__main__':
    main()