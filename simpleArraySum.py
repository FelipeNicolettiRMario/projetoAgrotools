def simpleArraySum(arr):
    print(sum(arr))

if __name__ == "__main__":
    arraySize = int(input())
    array = input().split()
    array = list(map(int,array))

    if len(array) == arraySize:
        simpleArraySum(array)

    else:
        print("Invalid array size!")