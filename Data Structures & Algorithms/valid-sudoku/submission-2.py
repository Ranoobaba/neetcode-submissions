from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # so the main thing here is when were going through the rows and colums we have to contain these values in some sort of hashmap and im thinknig hashset is important here.
        # we need 3 hashsets to contain each of the following things
        # 1-9 in a row, 1-9 in a column and 1-9 in a sqauare
        row_c = defaultdict(set)  # c stands for check here
        column_c = defaultdict(set)
        square_c = defaultdict(set)

        # the question of how I can make the square smaller - is by using something like mod, ie instead of 1 - 9 we can divide all the values on the axis by mod 3 or x // 3 , y //3 and then use a key value pair tuple as a storage device
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == ".":
                    continue
                if (
                    board[row][column] in row_c[row]
                    or board[row][column] in column_c[column]
                    or board[row][column] in square_c[(row // 3, column // 3)]
                ):
                    return False
                row_c[row].add(board[row][column])
                column_c[column].add(board[row][column])
                square_c[(row // 3, column // 3)].add(board[row][column])
        return True
