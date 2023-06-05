# Ques 3
def print_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)

    max_width = len(str(triangle[-1][len(triangle[-1]) // 2])) + 1

    for i in range(n):
        row = triangle[i]
        padding = ' ' * ((n - i - 1) * max_width // 2)
        line = ' ' * (max_width // 2)
        for num in row:
            line += str(num).center(max_width)
        print(padding + line)

print_pascals_triangle(5)


#output
#1
#11
#121
#1331
#14641


