def miniMaxSum(arr):
    print(sum(arr[:-1]),sum(arr[1:]))

if __name__ == '__main__':
    arr = input().split()

    if len(arr) == 5:
        arr = sorted(list(map(int,arr)))
        miniMaxSum(arr)
    else:
        print("Invalid array size")


