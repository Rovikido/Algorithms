from random import randint


def rand_partition(arr, left, right):
    pivot = randint(left, right)
    arr[left], arr[pivot] = arr[pivot], arr[left]
    return partition(arr, left, right)


def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quicksort(arr, left=0, right=None, random_pivot: bool = False):
    if right is None:
        right = len(arr)-1
    if left < right:
        part_pos = rand_partition(arr, left, right) if random_pivot else partition(arr, left, right)
        quicksort(arr, left, part_pos - 1, random_pivot)
        quicksort(arr, part_pos + 1, right, random_pivot)
    return arr


if __name__ == '__main__':
    try:
        array = input("Enter numbers: ").split()
        print(f'Normal partition: {quicksort(array, random_pivot=False)} \nRandom partition: {quicksort(array, random_pivot=True)}')
    except ValueError as e:
        print("Error occured: " + str(e))
