def TicTacDraw(board):
    # init line number
    line_number = 0
    for line in board:
        # if line number large than 0, print split line
        if line_number > 0:
            # create split line
            split_line = '-' * (4 * len(line) - 1)
            print(split_line)
        #init column number and line str
        column_num = 0
        line_str = ''
        # print line str
        for element in line:
            # create symbol
            if element == 0:
                symbol = 'O'
            elif element == 1:
                symbol = 'X'
            elif element == 2:
                symbol = ' '
            # if column number larger than 0, line str add '|'
            if column_num > 0:
                line_str += '|'
            # line str add symbol
            line_str += ' ' + symbol + ' '
            column_num += 1
        line_number += 1
        print(line_str)
        

board = [[1, 2, 1], [0, 1, 0], [1, 0, 2]]
TicTacDraw(board)