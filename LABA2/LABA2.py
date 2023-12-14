from itertools import product


class WordGeneratorConfig:
    """
    Класс для хранения конфигурационных параметров генератора слов.
    """
    # Параметры для проверки равенства символов на позициях
    EQUAL_AT_POSITIONS_I = 0
    EQUAL_AT_POSITIONS_J = 1

    # Конкретная комбинация для поиска
    SPECIFIC_COMBINATION = 'XY'

    # Набор символов для четных позиций
    EVEN_POSITION_CHARS = ['A', 'Y']

    # Символ и количество его вхождений для проверки
    CHAR_OCCURRENCES = 'X'
    COUNT_X_OCCURRENCES = 2


class WordGenerator:
    """
    Класс, предоставляющий возможности генерации слов с заданными параметрами.
    """

    def __init__(self, alphabet, n):
        """
        Инициализация класса с заданным алфавитом и длиной слова.
        :param alphabet: Алфавит, из которого формируются слова.
        :param n: Длина генерируемых слов.
        """
        self.alphabet = alphabet
        self.n = n
        self.all_combinations = list(product(alphabet, repeat=n))

    def equal_chars_at_positions(self, i, j):
        """
        Метод, возвращающий все слова, в которых символы на позициях i и j равны.
        :param i: Позиция i в слове.
        :param j: Позиция j в слове.
        :return: Список слов, удовлетворяющих условию.
        """
        return [word for word in self.all_combinations if word[i] == word[j]]

    def specific_combination_present(self, combination):
        """
        Метод, возвращающий все слова, содержащие определенную комбинацию символов.
        :param combination: Комбинация символов для поиска.
        :return: Список слов, содержащих данную комбинацию.
        """
        return [word for word in self.all_combinations if combination in "".join(word)]

    def chars_at_even_positions(self, char_set):
        """
        Метод, возвращающий слова, в которых на четных позициях находятся символы из заданного набора.
        :param char_set: Набор символов, допустимых на четных позициях.
        :return: Список слов, соответствующих условию.
        """
        return [word for word in self.all_combinations if all(word[i] in char_set for i in range(1, self.n, 2))]

    def every_third_char_digit(self):
        """
        Метод, возвращающий слова, где каждый третий символ - цифра.
        :return: Список слов, удовлетворяющих условию.
        """
        return [word for word in self.all_combinations if all(word[i].isdigit() for i in range(2, self.n, 3))]

    def x_before_y(self):
        """
        Метод, возвращающий слова, в которых все 'X' находятся перед 'Y'.
        :return: Список слов, соответствующих условию.
        """
        return [''.join(word) for word in self.all_combinations if 'X' in word and 'Y' in word and word.index('X') < word.index('Y')]

    def count_char_occurrences(self, char, k):
        """
        Метод, возвращающий слова, в которых количество вхождений заданного символа равно k.
        :param char: Заданный символ.
        :param k: Желаемое количество вхождений символа.
        :return: Список слов, удовлетворяющих условию.
        """
        return [word for word in self.all_combinations if word.count(char) == k]

    def more_x_than_y(self):
        """
        Метод, возвращающий слова, в которых количество 'X' больше, чем 'Y'.
        :return: Список слов, соответствующих условию.
        """
        return [word for word in self.all_combinations if word.count('X') > word.count('Y')]

    @staticmethod
    def count_words(words):
        """
        Метод, подсчитывающий количество слов в списке.
        :param words: Список слов.
        :return: Количество слов в списке.
        """
        return len(words)

    @staticmethod
    def get_alphabet_from_user():
        """
        Получает алфавит от пользователя.
        Возвращает алфавит как список символов.
        """
        user_input = input("Введите алфавит через пробел или запятую (например, 'X Y Z' или 'X,Y,Z'): ")
        return [char.strip() for char in user_input.replace(',', ' ').split()]

    @staticmethod
    def get_word_length_from_user():
        """
        Запрашивает у пользователя длину слова.
        Проверяет, что введенное значение является целым числом от 2 до 8.
        Возвращает длину слова как целое число.
        """
        while True:
            try:
                length = int(input("Введите длину слова (от 2 до 8): "))
                if 2 <= length <= 8:
                    return length
                else:
                    print("Длина слова должна быть в диапазоне от 2 до 8.")
            except ValueError:
                print("Пожалуйста, введите целое число.")

    @staticmethod
    def write_results_to_file(generator, results, filename):
        """
        Записывает результаты в файл.
        :param generator: Экземпляр класса WordGenerator.
        :param results: Словарь с результатами для каждого правила.
        :param filename: Имя файла для записи.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(
                f'Все возможные слова: {["".join(word) for word in generator.all_combinations]}, количество слов: {len(generator.all_combinations)}\n')
            for rule, (words, count) in results.items():
                file.write(f'{rule}: {words}, количество слов: {count}\n')


# Пример использования
#alphabet = ['X', 'Y', 'Z']
#word_length = 3

alphabet = WordGenerator.get_alphabet_from_user()
word_length = WordGenerator.get_word_length_from_user()
generator = WordGenerator(alphabet, word_length)

equal_at_positions = generator.equal_chars_at_positions(WordGeneratorConfig.EQUAL_AT_POSITIONS_I, WordGeneratorConfig.EQUAL_AT_POSITIONS_J)
count_equal_at_positions = generator.count_words(equal_at_positions)

specific_combination = generator.specific_combination_present(WordGeneratorConfig.SPECIFIC_COMBINATION)
count_specific_combination = generator.count_words(specific_combination)

even_position_chars = generator.chars_at_even_positions(WordGeneratorConfig.EVEN_POSITION_CHARS)
count_even_position_chars = generator.count_words(even_position_chars)

third_char_digit = generator.every_third_char_digit()
count_third_char_digit = generator.count_words(third_char_digit)

x_before_y = generator.x_before_y()
count_x_before_y = generator.count_words(x_before_y)

count_x = generator.count_char_occurrences(WordGeneratorConfig.CHAR_OCCURRENCES, WordGeneratorConfig.COUNT_X_OCCURRENCES)
count_count_x = generator.count_words(count_x)

more_x_than_y = generator.more_x_than_y()
count_more_x_than_y = generator.count_words(more_x_than_y)

# Словарь с результатами
results = {
    "Слова с равными символами на позициях 0 и 1": (equal_at_positions, count_equal_at_positions),
    "Слова, содержащие комбинацию XY": (specific_combination, count_specific_combination),
    "Слова с символами ['A', 'Y'] на четных позициях": (even_position_chars, count_even_position_chars),
    "Слова, где каждый третий символ - цифра": (third_char_digit, count_third_char_digit),
    "Слова, в которых все 'X' находятся перед 'Y'": (x_before_y, count_x_before_y),
    "Слова, где количество вхождений символа 'X' равно 2": (count_x, count_count_x),
    "Слова, в которых количество 'X' больше, чем 'Y'": (more_x_than_y, count_more_x_than_y)
}

output_filename = "word_generator_results.txt"
WordGenerator.write_results_to_file(generator, results, output_filename)
print(f"Результаты записаны в файл {output_filename}.")


'''
print(f'Все возможные слова: {generator.all_combinations}, количество слов: {len(generator.all_combinations)}')
print(f'Слова с равными символами на позициях {WordGeneratorConfig.EQUAL_AT_POSITIONS_I} и {WordGeneratorConfig.EQUAL_AT_POSITIONS_J}: {equal_at_positions}, '
      f'количество слов: {count_equal_at_positions}')
print(f'Слова, содержащие комбинацию {WordGeneratorConfig.SPECIFIC_COMBINATION}: {specific_combination}, количество слов: {count_specific_combination}')
print(f'Слова с символами {WordGeneratorConfig.EVEN_POSITION_CHARS} на четных позициях: {even_position_chars}, количество слов: {count_even_position_chars}')
print(f'Слова, где каждый третий символ - цифра: {third_char_digit}, количество слов: {count_third_char_digit}')
print(f'Слова, в которых все {WordGeneratorConfig.CHAR_OCCURRENCES} находятся перед Y: {x_before_y}, количество слов: {count_x_before_y}')
print(f'Слова, где количество вхождений символа {WordGeneratorConfig.CHAR_OCCURRENCES} равно {WordGeneratorConfig.COUNT_X_OCCURRENCES}: {count_x},'
      f' количество слов: {count_count_x}')
print(f'Слова, в которых количество X больше, чем Y: {more_x_than_y}, количество слов: {count_more_x_than_y}')
'''