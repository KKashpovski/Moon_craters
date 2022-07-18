"""Moon craters."""


def calculate(matrix: list) -> int:
    """Вычисление количества кратеров по исходным данным."""
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                if (i - 1 < 0 or matrix[i - 1][j] != 1) and (j - 1 < 0 or matrix[i][j - 1] != 1):
                    counter = counter + 1
            else:
                counter = counter
    print(counter)
    return counter


def main() -> None:
    """Многомерный массив."""
    with open("my_input.txt", "r") as fd:
        moon_data = fd.read()
        arr_a = []
        for line in moon_data.split("\n"):
            arr_tmp = []
            for e in line.split(" "):
                arr_tmp.append(int(e))
            arr_a.append(arr_tmp)
        print("Исходные данные о кратерах:", arr_a)
    calculate(arr_a)


if __name__ == "__main__":
    main()
