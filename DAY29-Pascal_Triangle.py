def generate_pascals_triangle(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle

def main():
    numRows = int(input("Enter the number of rows for Pascal's Triangle: "))
    triangle = generate_pascals_triangle(numRows)
    
    print(f"The first {numRows} rows of Pascal's Triangle are:")
    for row in triangle:
        print(row)

if __name__ == "__main__":
    main()
