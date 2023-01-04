def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)
        quickSort(array, low, partition_index - 1)
        quickSort(array, partition_index + 1, high)


def is_anagram(first_string, second_string):
    sorted_str1 = quickSort(first_string, 0, len(first_string) - 1)
    sorted_str2 = quickSort(second_string, 0, len(second_string) - 1)

    anagram = sorted_str1 == sorted_str2

    return (sorted_str1, sorted_str2, anagram)
