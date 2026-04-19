# Исходная функция (ваш вариант)
def common_tags(items: list[dict]) -> set[str]:
    freq = {}
    for item in items:
        tags = {tag.strip().lower() for tag in item.get('tags', []) if isinstance(tag, str) and tag}
        for tag in tags:
            freq[tag] = freq.get(tag, 0) + 1
    return {tag for tag, cnt in freq.items() if cnt >= 2}

# ----- ТЕСТЫ -----

# 1. Пример из условия
items1 = [
    {"id": 1, "tags": ["AI", "python"]},
    {"id": 2, "tags": ["ai", "data"]},
    {"id": 3, "tags": ["PYTHON", "ml"]},
    {"id": 4, "tags": []},
]
assert common_tags(items1) == {"ai", "python"}

# 2. Пустой список
assert common_tags([]) == set()

# 3. Один элемент — нет общих тегов (ни с кем)
items3 = [{"tags": ["a", "b", "c"]}]
assert common_tags(items3) == set()

# 4. Все элементы имеют одинаковый тег (нормализованный)
items4 = [
    {"tags": ["Hello"]},
    {"tags": ["  HELLO  "]},
    {"tags": ["hello"]},
]
assert common_tags(items4) == {"hello"}

# 5. Тег встречается в одном элементе несколько раз (дубликаты не должны влиять)
items5 = [
    {"tags": ["x", "x", "y"]},
    {"tags": ["x", "z"]},
]
assert common_tags(items5) == {"x"}   # x есть в обоих, y только в первом, z только во втором

# 6. Пустые строки, None, нестроковые значения — игнорируются
items6 = [
    {"tags": ["", "   ", None, 123, "valid"]},
    {"tags": ["valid"]},
]
assert common_tags(items6) == {"valid"}

# 7. Отсутствие ключа 'tags' у некоторых элементов
items7 = [
    {"id": 1, "tags": ["apple"]},
    {"id": 2},  # нет ключа 'tags'
    {"id": 3, "tags": ["APPLE"]},
]
assert common_tags(items7) == {"apple"}

# 8. Регистр и пробелы: нормализация работает
items8 = [
    {"tags": ["  Big Data  "]},
    {"tags": ["big data"]},
]
assert common_tags(items8) == {"big data"}

# 9. Теги, которые встречаются ровно в двух элементах
items9 = [
    {"tags": ["only_once"]},
    {"tags": ["only_once", "twice"]},
    {"tags": ["twice"]},
]
# assert common_tags(items9) == {"twice"}   # only_once только в первом и втором? check: only_once есть в 0 и 1 индексах -> дважды. twice во 1 и 2 -> тоже дважды.
# На самом деле both: только_once есть в items9[0] и items9[1] -> 2 раза, twice в items9[1] и items9[2] -> 2 раза. Ожидаем {"only_once", "twice"}
assert common_tags(items9) == {"only_once", "twice"}

# 10. Большое количество элементов, нет общих тегов
items10 = [{"tags": [f"tag_{i}"]} for i in range(100)]
assert common_tags(items10) == set()

print("Все тесты пройдены!")