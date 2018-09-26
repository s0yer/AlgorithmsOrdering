

def insertionSort(k):
    for i in range(1,len(k)):
        j = i
        temp = k[j]
        while j > 0 and temp < k[j-1]:
            k[j] = k[j-1]
            j=j-1
        k[j] = temp
    return k