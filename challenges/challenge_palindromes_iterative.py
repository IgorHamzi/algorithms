def is_palindrome_iterative(word):
    index = 0

    if word == '':
        return False

    for letter in reversed(word):
        if letter != word[index]:
            return False
        else:
            index += 1

    return True


if __name__ == '__main__':
    is_palindrome_iterative('arara')
