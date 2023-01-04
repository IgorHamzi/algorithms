def quickSort(arr):

    elements = len(arr)

    if elements < 2:
        return arr

    current_position = 0

    for i in range(1, elements):
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp

    left = quickSort(arr[0:current_position])
    right = quickSort(arr[current_position+1:elements])

    arr = left + [arr[current_position]] + right

    return arr


def is_anagram(first_string, second_string):

    sorted_str1 = quickSort(list(first_string.lower()))
    sorted_str2 = quickSort(list(second_string.lower()))

    anagram = sorted_str1 == sorted_str2

    if first_string == '' or second_string == '':
        anagram = False

    return (''.join(sorted_str1), ''.join(sorted_str2), anagram)
