
class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count > other._count:
            return Cell(self._count - other._count)
        else:
            print(f"Операция невозможна")

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


if __name__ == '__main__':
    cells_1 = Cell(5)
    print(cells_1)
    cells_2 = Cell(4)
    print(cells_2)

    print(cells_1 + cells_2)
    print(cells_1 - cells_2)
    print(cells_2 - cells_1)
    print(cells_1 * cells_2)
    print(cells_1 / cells_2)
    print((cells_1 * cells_2).make_order(6))
