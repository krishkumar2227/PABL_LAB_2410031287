#Given an m x n grid of characters board and a string word, return true if word exists in the grid.The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        # If all characters matched
        if index == len(word):
            return True

        # Boundary + mismatch check
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
            return False

        # Mark visited
        temp = board[r][c]
        board[r][c] = "#"

        # Explore all directions
        found = (
            dfs(r+1, c, index+1) or
            dfs(r-1, c, index+1) or
            dfs(r, c+1, index+1) or
            dfs(r, c-1, index+1)
        )

        # Backtrack
        board[r][c] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False