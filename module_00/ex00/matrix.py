class Matrix:
    def __init__(self, data):
        if isinstance(data, list):
            self.data = data
            self.shape = (len(data), len(data[0]))
        elif isinstance(data, tuple) and len(data) == 2:
            self.shape = data
            self.data = [[0] * data[1] for _ in range(data[0])]

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
                raise ValueError("Matrices must have the same shape")
            result = [
                [self.data[i][j] + other.data[i][j] for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        elif isinstance(other, (int, float)):
            result = [
                [self.data[i][j] + other for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        else:
            return NotImplemented
        return Matrix(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
                raise ValueError("Matrices must have the same shape")
            result = [
                [self.data[i][j] - other.data[i][j] for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        elif isinstance(other, (int, float)):
            result = [
                [self.data[i][j] - other for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        else:
            return NotImplemented
        return Matrix(result)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        if isinstance(other, Matrix):
            if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
                raise ValueError("Matrices must have the same shape")
            result = [
                [self.data[i][j] / other.data[i][j] if other.data[i][j] != 0 else float('inf') for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = [
                [self.data[i][j] / other for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        else:
            return NotImplemented
        return Matrix(result)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError("Matrices don't have compatible shapes")
            result = [
                [sum(self.data[i][k] * other.data[k][j] for k in range(self.shape[1]))
                for j in range(other.shape[1])]
                for i in range(self.shape[0])]
        elif isinstance(other, (int, float)):
            result = [
                [self.data[i][j] * other for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        else:
            return NotImplemented
        return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f"Matrix with shape {self.shape}:\n" + '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __repr__(self):
        return f"Matrix({repr(self.data)})"

    def T(self):
        result = [
            [self.data[i][j] for i in range(self.shape[0])]
            for j in range(self.shape[1])
        ]
        return Matrix(result)

class Vector(Matrix):
    def __init__(self, data):
        if not (len(data) == 1 or len(data[0]) == 1):
            raise ValueError("the input is not valid for a Vector that needs to have either 1 column or 1 row")
        super().__init__(data)

    def __add__(self, other):
        result = super().__add__(other)
        return Vector(result.data)

    def dot(self, other):
        if (self.shape != other.shape):
            raise ValueError("both vectors must have the same dimensions")
        if (self.shape[0] == 1):
            return sum(x * y for x, y in zip(self.data[0], other.data[0]))
        else:
            return sum(x * y for x, y in zip((self.data[i][0] for i in range(self.shape[0])), (other.data[i][0] for i in range(other.shape[0]))))

    def __str__(self):
        if self.shape[0] == 1:
            return f"Vector with shape {self.shape}:\n" + '\t'.join(map(str, self.data[0]))
        elif self.shape[1] == 1:
            return f"Vector with shape {self.shape}:\n" + '\n'.join(map(str, [row[0] for row in self.data]))

    def __repr__(self):
        return f"Vector({repr(self.data)})"