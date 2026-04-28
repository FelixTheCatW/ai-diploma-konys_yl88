"""
Модуль для работы с CSV-файлами.

Содержит функции сохранения, загрузки, подсчёта строк
и суммирования значений в столбце CSV.
"""

import csv


def save_csv(filename, rows):
    """
    Сохраняет список списков в CSV-файл.

    Аргументы:
        filename (str): Имя файла.
        rows (list[list]): Данные в виде строк и столбцов.
    """
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


def load_csv(filename):
    """
    Загружает CSV-файл в список списков.

    Аргументы:
        filename (str): Имя файла.

    Возвращает:
        list[list]: Данные CSV.
    """
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)


def count_csv_rows(filename):
    """
    Подсчитывает количество строк в CSV-файле (включая заголовок).

    Аргументы:
        filename (str): Имя файла.

    Возвращает:
        int: Количество строк.
    """
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    return len(data)


def sum_column(filename, col_index):
    """
    Суммирует значения в указанном столбце CSV-файла.
    Предполагается, что значения столбца – целые числа.

    Аргументы:
        filename (str): Имя файла.
        col_index (int): Индекс столбца (начиная с 0).

    Возвращает:
        int: Сумма значений.
    """
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)

    total = 0
    for row in data:
        total += int(row[col_index])
    return total
