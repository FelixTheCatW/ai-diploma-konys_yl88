"""
Модуль для базовой работы с текстовыми файлами.

Предоставляет функции сохранения, загрузки, добавления текста в файл
и подсчёта количества строк.
"""


def save_text(filename, text):
    """
    Сохраняет текст в файл (перезаписывает файл).

    Аргументы:
        filename (str): Имя файла.
        text (str): Текст для записи.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def load_text(filename):
    """
    Загружает текст из файла.

    Аргументы:
        filename (str): Имя файла.

    Возвращает:
        str: Содержимое файла.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def append_text(filename, text):
    """
    Добавляет текст в конец файла (с новой строки).

    Аргументы:
        filename (str): Имя файла.
        text (str): Добавляемый текст.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n" + text)


def count_lines(filename):
    """
    Подсчитывает количество строк в файле.

    Аргументы:
        filename (str): Имя файла.

    Возвращает:
        int: Количество строк.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines)
