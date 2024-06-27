def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the ending letter: ')

    """
    ########################################
    Code Your Program here
    ########################################
    """
    if string.isalpha(start) > string.isalpha(end):
        start = input('The starting letter must be before the ending letter: ')
        end = input('The ending letter must be after the starting letter: ')

    begin = string.isalpha(start)
    stop = string.isalpha(end)

    for x in range(begin, stop):
        result.append(len(string.isalpha(x)))
    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
