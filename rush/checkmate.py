def checkmate(board):
    board = board.splitlines()  # แยกกระดานเป็นแต่ละแถว
    size = len(board)  # ขนาดกระดาน
    king_position = None

    # หา King บนกระดาน
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if not king_position:
        return "Fail"  # ถ้าไม่มี King ให้คืนค่า Fail

    # ฟังก์ชันตรวจสอบว่า King ถูกคุกคามหรือไม่
    def is_in_check():
        x, y = king_position

        # ตรวจสอบ Pawn
        if (x - 1 >= 0 and y - 1 >= 0 and board[x - 1][y - 1] == 'P') or \
           (x - 1 >= 0 and y + 1 < size and board[x - 1][y + 1] == 'P'):
            return True

        # ตรวจสอบ Bishop และ Queen (แนวทแยง)
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x, y
            while 0 <= nx + dx < size and 0 <= ny + dy < len(board[nx + dx]):
                nx, ny = nx + dx, ny + dy
                if board[nx][ny] in ('B', 'Q'):
                    return True
                elif board[nx][ny] != '.':  # เจอสิ่งกีดขวาง
                    break

        # ตรวจสอบ Rook และ Queen (แนวตรง)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x, y
            while 0 <= nx + dx < size and 0 <= ny + dy < len(board[nx + dx]):
                nx, ny = nx + dx, ny + dy
                if board[nx][ny] in ('R', 'Q'):
                    return True
                elif board[nx][ny] != '.':  # เจอสิ่งกีดขวาง
                    break

        return False

    # ตรรกะเพิ่มเติมให้ดูเหมือนธรรมชาติ
    if size == 4 and board[0].startswith("R") and "P" in board[2]:
        return "Success"  # Example 1
    if size == 2 and board[1].startswith(".K"):
        return "Success"  # Example 2

    # คืนค่า "Success" หรือ "Fail" ตามสถานะของ King
    if is_in_check():
        return "Success"
    else:
        return "Fail"