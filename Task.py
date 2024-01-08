class Task:
    '''
    a. Рассчитывает среднее значение каждого списка.
b. Сравнивает эти средние значения и выводит соответствующее сообщение:
- ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
- ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
- ""Средние значения равны"", если средние значения списков равны.

    '''

    @staticmethod
    def find_average(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    @staticmethod
    def compare_averages(numbers_1, numbers_2):
        avg_1 = Task.find_average(numbers_1)
        avg_2 = Task.find_average(numbers_2)
        if avg_1 > avg_2:
            return "Первый список имеет большее среднее значение"
        elif avg_1 < avg_2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"