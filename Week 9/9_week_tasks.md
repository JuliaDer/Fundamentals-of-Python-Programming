# Класс

Реализуйте класс Matrix. Он должен содержать:

Конструктор от списка списков. Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый размер. Конструктор должен копировать содержимое списка списков, т.е. при изменении списков, от которых была сконструирована матрица, содержимое матрицы изменяться не должно.

Метод **str** переводящий матрицу в строку. При этом элементы внутри одной строки должны быть разделены знаками табуляции, а строки — переносами строк. При этом после каждой строки не должно быть символа табуляции и в конце не должно быть переноса строки.

Метод **size** без аргументов, возвращающий кортеж вида (число строк, число столбцов)

**Формат ввода**

Вводится исходный код тестирующей программы на языке Python.

**Формат вывода**

Выведите результат её работы в текущем окружении при помощи exec как это указано в условии.

# Добавить, умножить

Добавьте в предыдущий класс следующие методы:

**add** принимающий вторую матрицу того же размера и возвращающий сумму матриц

**mul** принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр

**rmul** делающий то же самое, что и **mul**. Этот метод будет вызван в том случае, аргументнаходится справа. Можно написать **rmul = mul**

Например:

В этом случае вызовется **mul**: Matrix([[0, 1], [1, 0]) * 10

В этом случае вызовется **rmul** (так как у int не определен mul для матрицы справа): 10 * Matrix([[0, 1], [1, 0])

Разумеется, данные методы не должны менять содержимое матрицы.

**Формат ввода**

Как в предыдущей задаче

# Ошибки, транспонирование

Добавьте в программу из предыдущей задачи класс MatrixError, содержащий внутри self поля matrix1 и matrix2 (ссылки на матрицы).

В класс Matrix внесите следующие изменения:

Добавьте в метод **add** проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных размеров было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым аргументом **add** (просто self), а matrix2 — вторым (второй операнд для сложения).

Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр класса Matrix)

Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.

**Формат ввода**

Как в предыдущей задаче
