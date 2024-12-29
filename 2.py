class SparseMatrix:
    def __init__(self):
        self.data = {}

    def gray(self, i, j, value):
        if value != 0:
            self.data[(i, j)] = value

    def display(self):
        for (i, j), value in self.data.items():
            print(f"Pixel ({i}, {j}) = {value}")

# 建立稀疏矩陣
matrix = SparseMatrix()
matrix.gray(0, 1, 50)
matrix.gray(1, 3, 120)
matrix.gray(2, 4, 180)
matrix.gray(3, 2, 255)

# 顯示結果
matrix.display()