# Your code here
def two_dimensional_list(n_rows, n_columns):
    dimensions = [n_rows, n_columns]
    row_num = dimensions[0]
    col_num = dimensions[1]
    matrix = [[0 for col in range(col_num)] for row in range(row_num)]

    # for row in range(row_num):
    #     for col in range(col_num):
    #         matrix[row][col] = row * col

    return matrix

print(two_dimensional_list(3,5))