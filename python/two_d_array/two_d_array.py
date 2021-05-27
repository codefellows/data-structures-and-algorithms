def hourglassSum(arr):
    counter = 4
    hourglass_list = []
    for i in range(counter):
        for j in range(counter):
            hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass_list.append(hourglass)
            j+=1
        i+=1
    hourglass_list.sort(reverse=True)
    return hourglass_list[0]  