# Краткое описание функционала:
# Находит теги, которые встречаются минимум в двух словарях.
#
# Краткое описание алгоритма:
# Функция проходит по списку объектов, нормализует теги каждого элемента, считает частоту появления тегов и возвращает множество тегов с частотой не меньше двух.

def common_tags(items: list[dict]) -> set[str]:
    normalize_tag = lambda s: s.strip().lower() if s and isinstance(s, str) else None
    norms = [{norm for i in item.get('tags', []) if (norm := normalize_tag(i)) is not None} for item in items]
    print(norms)
    result = {n & s for n in norms}
    print(result)


items = [
    {"id": 1, "tags": ["AI", "python"]},
    {"id": 2, "tags": ["ai", "data"]},
    {"id": 3, "tags": ["PYTHON", "ml"]},
    {"id": 4, "tags": []},
]
# assert common_tags(items) == {"ai", "python"}
common_tags(items)