from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Generate a multiplication table based on the specified range of rows and columns.

    Args:
        row_start (int): The starting value of the rows.
        row_end (int): The ending value of the rows.
        column_start (int): The starting value of the columns.
        column_end (int): The ending value of the columns.

    Returns:
        List[List[int]]: A 2D list representing the multiplication table.
    """
    multiplication_list = []
    for i in range(row_start, row_end + 1):
        multiplication = []
        for j in range(column_start, column_end + 1):
            multiplication.append(i * j)
        multiplication_list.append(multiplication)
    return multiplication_list


row_start = 1
row_end = 9
column_start = 1
column_end = 9

a = check(row_start, row_end, column_start, column_end)
print(a)
