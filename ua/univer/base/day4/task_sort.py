if __name__ == '__main__':
    arr = [1,2,3,4,67,888,43,57,56,3534,7,6,2,0]
    #arr.sort()
    count = 0
    for i in range(len(arr)):
        print(arr[i])
        for j in range(len(arr) - 1 - i):
            count += 1
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)
    print(count)