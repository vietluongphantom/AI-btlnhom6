# A very unnecessary file, use for calculate miscellaneous things.

k = 0

white_starting_positions = [0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57]

for i in white_starting_positions:
    k += (1 << i)
print(k)

k = 0

black_starting_positions = [6, 7, 14, 15, 22, 23, 30, 31, 38, 39, 46, 47, 54, 55, 62, 63]

for i in black_starting_positions:
    k += (1 << i)
print(k)

k = 0

black_available_takes = [2, 10, 18, 26, 34, 42, 50, 58]

for i in black_available_takes:
    k += (1 << i)
print(k)

k = 0

white_available_takes = [5, 13, 21, 29, 37, 45, 53, 61]

for i in white_available_takes:
    k += (1 << i)
print(k)

# The starting board:

#     _________________________________________
#     |    |    |    |    |    |    |    |    |       
#     | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 |
#     |____|____|____|____|____|____|____|____|
#     |    |    |    |    |    |    |    |    |
#     | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 |
#     |____|____|____|____|____|____|____|____|
#     |    |    |    |    |    |    |    |    |
#     | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
#     |____|____|____|____|____|____|____|____|
#     |    |    |    |    |    |    |    |    |
#     | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
#     |____|____|____|____|____|____|____|____|
#     |    |    |    |    |    |    |    |    |
#     | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |
#     |____|____|____|____|____|____|____|____|
#     |    |    |    |    |    |    |    |    |
#     | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
#     |____|____|____|____|____|____|____|____|
#     |    |    |    |    |    |    |    |    |
#     | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 |
#     |____|____|____|____|____|____|____|____|
#     |    |    |    |    |    |    |    |    |
#     | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |
#     |____|____|____|____|____|____|____|____|


# import sqlite3
# connection = sqlite3.connect('chessboard.db')
# cursor = connection.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
#               (Chessboard_ID INTEGER PRIMARY KEY, wins INTEGER, loses INTEGER, draws INTEGER)''')

# connection.commit()
# connection.close()