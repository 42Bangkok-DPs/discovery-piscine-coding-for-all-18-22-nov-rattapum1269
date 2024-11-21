from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Example 1:")
    print(checkmate(board1))  # Expected Output: Success

    # ตัวอย่างที่ 2
    board2 = """\
..
.K\
"""
    print("Example 2:")
    print(checkmate(board2))  # Expected Output: Success

if __name__ == "__main__":
    main()