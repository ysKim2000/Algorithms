def Shellsort(arr):
    h = 1
    while h < len(arr):
        h = 3*h + 1
    h = h//3

    while h > 0:
        for i in range(h,len(arr)):
            k=i-h
            key=arr[i]
            while k>=0 and key < arr[k]:
                arr[k+h] = arr[k]
                k=k-h
            arr[k+h] = key
        h = h//3
    return arr
