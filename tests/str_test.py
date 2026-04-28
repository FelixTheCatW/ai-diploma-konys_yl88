def wrap_text(text: str, width: int) -> list[str]:
    """Разбивает длинный текст на строки заданной ширины."""
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
    return lines if lines else [text]


a = "asd asd asd " * 100
b = wrap_text(a, 80)
print(b)