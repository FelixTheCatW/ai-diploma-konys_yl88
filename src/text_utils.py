def normalize_text(s: str) -> str:
    s = str(s).strip().lower()
    while "  " in s:
        s = s.replace("  ", " ")
    return s

def word_count(text):
    return len(text.split())


def contains_word(text, word):
    return word.lower() in text.lower()
