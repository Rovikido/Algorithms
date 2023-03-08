from math import ceil
from lab_6_1 import rand_partition


def RandSelect(arr, i, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    i = int(i)
    return rand_select(arr, i, left, right)


def rand_select(arr, i, left, right):
    if left == right:
        return arr[left]
    q = rand_partition(arr, left, right)
    k = q - left + 1
    if i == k:
        return arr[q]
    elif i < k:
        return rand_select(arr, i, left, right-1)
    else:
        return rand_select(arr, i-k, q+1, right)


if __name__ == '__main__':
    try:
        a = input("Enter numbers: ").split()
        a = list(map(lambda _: float(_), a))

        print(f'\n\nMin: {RandSelect(a, 0)} \n'
              f'Median: {str(RandSelect(a, int(len(a) / 2))) +" "+ str(RandSelect(a, int(len(a) / 2)+1))  if len(a) % 2 == 0 else  RandSelect(a, ceil(len(a) / 2)) } \n'
              f'Max: {RandSelect(a, len(a))}')
    except ValueError as e:
        print("Error occured: " + str(e))
