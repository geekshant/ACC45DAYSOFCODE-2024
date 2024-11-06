def game_of_life(board):
    def count_live_neighbors(board, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        live_neighbors = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and abs(board[r][c]) == 1:
                live_neighbors += 1
        return live_neighbors

    for row in range(len(board)):
        for col in range(len(board[0])):
            live_neighbors = count_live_neighbors(board, row, col)

            if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = -1  # Mark as dead
            if board[row][col] == 0 and live_neighbors == 3:
                board[row][col] = 2  # Mark as live

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0

def main():
    print("Enter the dimensions of the board (m n):")
    m, n = map(int, input().split())
    board = []
    print("Enter the initial state of the board row by row (each row should have n space-separated integers):")
    for _ in range(m):
        row = list(map(int, input().split()))
        board.append(row)

    print("Initial state:")
    for row in board:
        print(" ".join(map(str, row)))

    game_of_life(board)

    print("Next state:")
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
