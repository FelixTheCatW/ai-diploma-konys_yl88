"""
Модуль для обработки текстовых строк.

Содержит функции нормализации текста, подсчёта слов и проверки наличия слова.
"""


def normalize_text(s: str) -> str:
    """
    Приводит строку к нормализованному виду: удаляет лишние пробелы,
    приводит к нижнему регистру и заменяет множественные пробелы одинарными.

    Аргументы:
        s (str): Входная строка.

    Возвращает:
        str: Нормализованная строка.
    """
    return " ".join(str(s).lower().split())


def word_count(text):
    """
    Подсчитывает количество слов в тексте.

    Аргументы:
        text (str): Входной текст.

    Возвращает:
        int: Количество слов.
    """
    return len(text.split())


def contains_word(text, word):
    """
    Проверяет, содержится ли заданное слово в тексте (регистронезависимо).

    Аргументы:
        text (str): Текст для поиска.
        word (str): Искомое слово.

    Возвращает:
        bool: True, если слово найдено, иначе False.
    """
    return word.lower() in text.lower()

def wrap_text(text: str, width: int) -> list[str]:
    """Разбивает длинный текст на строки заданной ширины.

    Аргументы:
        text (str): Исходный текст.
        width (str): Максимальная длина строки.

    Возвращает:
        bool: True, если слово найдено, иначе False.

    """
    if not text:
        return [""]
    words = text.split()
    lines = []
    current_line = []
    current_len = 0

    for word in words:
        if current_len + len(word) + 1 <= width:
            current_line.append(word)
            current_len += len(word) + 1
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_len = len(word) + 1
    if current_line:
        lines.append(" ".join(current_line))

    return lines