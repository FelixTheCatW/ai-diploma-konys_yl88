"""
Модуль для обработки текстовых строк.
"""


def normalize_text(s: str) -> str:
    """
    Приводит строку к нормализованному виду.
    """
    return " ".join(str(s).lower().split())


def word_count(text: str) -> int:
    """
    Подсчитывает количество слов в тексте.
    """
    if not text or not text.strip():
        return 0
    return len(text.split())


def contains_word(text: str, word: str) -> bool:
    """
    Проверяет, содержится ли заданное слово в тексте (как отдельное слово).
    """
    # Нормализуем оба значения и разбиваем текст на список слов
    normalized_text = normalize_text(text)
    normalized_word = normalize_text(word)

    if not normalized_word:
        return False

    words = normalized_text.split()
    return normalized_word in words


def wrap_text(text: str, width: int) -> list:
    """
    Разбивает длинный текст на строки заданной ширины.
    """
    if not text:
        return [""]

    words = text.split()
    if not words:
        return [""]

    lines = []
    current_line = []
    current_len = 0

    for word in words:        
        extra_space = 1 if current_line else 0
        if current_len + len(word) + extra_space <= width:
            current_line.append(word)
            current_len += len(word) + extra_space
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_len = len(word)

    if current_line:
        lines.append(" ".join(current_line))

    return lines
