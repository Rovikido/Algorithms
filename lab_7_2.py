import math


def counting_sort(arr, place):
    counts = [0, ] * 10

    for i in arr:
        index = i // place
        counts[index % 10] += 1

    for i in reversed(range(len(counts))):
        counts[i] = sum(counts[:i+1])

    n = len(arr)

    output = [0, ] * n
    for i in reversed(arr):
        index = i // place
        output[counts[index % 10]-1] = i
        counts[index % 10] -= 1

    return output


def radix_sort(arr):
    n = max(arr)
    for i in range(0, int(math.log10(n))+1):
        arr = counting_sort(arr, 10**i)
    return arr


if __name__ == '__main__':
    try:
        while True:
            a = input("Enter positive non-zero numbers: ").split()
            a = list(map(lambda _: int(_), a))
            if min(a) < 1:
                raise ValueError("ENTER POSITIVE NON-ZERO NUMBER!")

            print(f'Sorted data: {radix_sort(a)} \n\n')
    except ValueError as e:
        print("Incorrect input: " + str(e))