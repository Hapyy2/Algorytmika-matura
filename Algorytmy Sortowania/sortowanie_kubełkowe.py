def insertion_sort(A):
    for i in range(1, len(A)):
        liczba = A[i]

        while i > 0 and A[i - 1] > liczba:
            A[i] = A[i - 1]
            i -= 1
        A[i] = liczba


def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    output = []

    for i in range(len(arr)):

        j = int(arr[i] / (max(arr) / len(arr)))
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    for z in range(len(arr)):
        insertion_sort(buckets[z])

    for x in range(len(arr)):
        output += buckets[x]
    return output