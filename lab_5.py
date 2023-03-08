from math import ceil, floor


def Merge(a, b):
    temp = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1
    while i < len(a):
        temp.append(a[i])
        i += 1
    while j < len(b):
        temp.append(b[j])
        j += 1
    return temp



def MergeSort(a):
    mid = int(ceil(len(a)/2))
    if len(a) >= 2:
        l = MergeSort(a[:mid])
        r = MergeSort(a[mid:])
        a = Merge(l, r)
    return a


try:
    a = input("Enter numbers: ").split()
    a = list(map(lambda i: int(i), a))
    print(MergeSort(a))
except ValueError as e:
    print("Error occured: " + str(e))

