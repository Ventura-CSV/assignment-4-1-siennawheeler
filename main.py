def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the ending letter: ')
        begin = ord(start)
        stop = ord(end)
        while stop <= begin or start.isalpha() == False or end.isalpha() == False:
            start = input()
            end = input('The ending letter must be after the starting letter: ')
            begin = ord(start)
            stop = ord(end)
        break
        

    """
    ########################################
    Code Your Program here
    ########################################
    """

    '''for x in range(begin, stop):
        result.append(x)'''
    x = begin
    while x <= stop:
        result.append(chr(x))
        x = x + 1
    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
