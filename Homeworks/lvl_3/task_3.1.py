# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)


class Matrix():
    def __init__(self,rows,columns,n):
        self.n = n
        self.rows = rows
        self.columns = columns    

    def columns(self,new_columns):
        if new_columns!=self.columns:
            self.columns = new_columns
        return self.columns
    
    def rows(self,new_rows):
        if new_rows!=self.rows:
            self.rows = new_rows
        return self.rows
    
    def n(self,new_n):
        if new_n!=self.n:
            self.n = new_n
        return self.n
    
    def display(self):
        for i in range(1, self.rows+1):
            matrix = ([self.n]*self.columns)
            print(matrix, end = '\n')
        print(f"Количество строк: {my_matrix.rows}")
        print(f"Количество колонок: {my_matrix.columns}")
      
        
my_matrix = Matrix(5,9,7)
my_matrix.columns=4
my_matrix.rows=5
my_matrix.n = 7
my_matrix.display()
