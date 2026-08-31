def square_numbers(beginning, end):
    odd_squares = []
    even_squares = []

    for number in range(beginning, end + 1):
        square = number ** 2

        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("Odd square values:", odd_squares)
    print("Even square values:", even_squares)


square_numbers(1, 10)