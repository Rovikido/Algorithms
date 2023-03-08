def counting_sort(arr, desc=False):
    counts = [0, ] * (max(arr) + 2)

    for i in arr:
        counts[i] += 1

    for i in reversed(range(len(counts))):
        counts[i] = sum(counts[:i+1])

    n = len(arr)

    output = [0, ] * n
    for i in arr:
        output[counts[i]-1] = i
        counts[i] -= 1

    if desc:
        res = [0, ] * n
        for i in range(n):
            res[i] = output[n-i-1]
        return res

    return output


if __name__ == '__main__':
    try:
        a = input("ENTER NUMBER IN RANGE [0,9]: ").split()
        a = list(map(lambda _: int(_), a))
        if min(a) < 0 or max(a) > 9:
            raise ValueError("ENTER NUMBER IN RANGE [0,9]!")

        print(f'Sorted data: {counting_sort(a)} \n'
              f'In descending order: {counting_sort(a, True)}')
    except ValueError as e:
        print("Incorrect input: " + str(e))

