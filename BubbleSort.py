def countSwaps(a):
    n = len(a)
    swaps = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swaps = swaps + 1
    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n - 1])