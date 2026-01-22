from sys import stdin
def gegnerate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
def print_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))
def main():
    n = int(stdin.readline().strip())+1
    triangle = gegnerate_pascals_triangle(n)
    print_triangle(triangle)

main()
