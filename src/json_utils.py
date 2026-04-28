"""
Модуль для работы с JSON-данными.

Содержит функции сохранения и загрузки JSON в файл,
а также преобразования словаря в JSON-строку.
"""

import json


def save_json(filename, data):
    """
    Сохраняет данные в JSON-файл с отступами и поддержкой UTF-8.

    Аргументы:
        filename (str): Имя файла.
        data (dict/list): Данные для сохранения.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_json(filename):
    """
    Загружает данные из JSON-файла.

    Аргументы:
        filename (str): Имя файла.

    Возвращает:
        dict/list: Загруженные данные.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def dict_to_json_text(data):
    """
    Преобразует словарь или список в отформатированную JSON-строку.

    Аргументы:
        data (dict/list): Входные данные.

    Возвращает:
        str: JSON-строка с отступами.
    """
    return json.dumps(data, ensure_ascii=False, indent=4)
