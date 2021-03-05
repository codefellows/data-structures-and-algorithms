
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        # print('L is:', L)
        R = arr[mid:]
        # print('R is:', R)

        mergeSort(L)
        mergeSort(R)
        merge(L, R, arr)
    return arr

def merge(L, R, arr):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# arr_1 = [8,4,23,42,16,15]
arr_1 = [20,18,12,8,5,-2]

if __name__ == '__main__':
    print(mergeSort(arr_1))
    

    
