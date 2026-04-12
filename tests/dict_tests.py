def update_item_fields(item: dict, patch: dict) -> dict:
    if not item:
        return patch.copy()
    if not patch:
        return item.copy()    
    return item | patch

def sum_by_key(rows: list[dict], key: str) -> float:
    return sum(v for row in rows
        if isinstance((v := row.get(key)), (int, float)) and not isinstance(v, bool))

# ========== Тесты для update_item_fields ==========
def test_update_item_fields():
    # Базовые случаи
    assert update_item_fields({}, {"a": 1}) == {"a": 1}
    assert update_item_fields({"a": 1}, {}) == {"a": 1}
    assert update_item_fields({}, {}) == {}
    assert update_item_fields({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
    
    # Проверка, что возвращается копия, а не оригинал
    original_item = {"x": 10}
    result = update_item_fields(original_item, {})
    assert result is not original_item
    assert result == original_item
    
    original_patch = {"y": 20}
    result = update_item_fields({}, original_patch)
    assert result is not original_patch
    assert result == original_patch
    
    # Перезапись значения на None
    assert update_item_fields({"a": 1}, {"a": None}) == {"a": None}
    
    # Сложные вложенные структуры (функция не рекурсивна, просто поверхностное слияние)
    assert update_item_fields({"a": {"b": 1}}, {"a": 2}) == {"a": 2}
    
    # Каверзные типы ключей (не только строки)
    assert update_item_fields({1: "one", 2: "two"}, {2: "TWO", 3: "three"}) == {1: "one", 2: "TWO", 3: "three"}
    assert update_item_fields({(1,2): "tuple"}, {(1,2): "updated"}) == {(1,2): "updated"}
    
    # Поведение при item=None (None считается falsy, возвращается patch.copy())
    assert update_item_fields(None, {"a": 1}) == {"a": 1}
    assert update_item_fields(None, {}) == {}
    # patch=None, но item не пустой -> возвращается item.copy()
    assert update_item_fields({"a": 1}, None) == {"a": 1}
    # Проверка копирования при item=None и patch не None
    patch_orig = {"b": 2}
    res = update_item_fields(None, patch_orig)
    assert res is not patch_orig
    assert res == patch_orig
    # Оба None: item=None -> not item истинно, пытается вернуть patch.copy(), но patch=None -> AttributeError
    try:
        update_item_fields(None, None)
    except AttributeError:
        pass  # Ожидаемое исключение
    else:
        assert False, "Expected AttributeError when both arguments are None"

# ========== Тесты для sum_by_key ==========
def test_sum_by_key():
    # Пустой список
    assert sum_by_key([], "any") == 0.0
    
    # Ключ отсутствует во всех строках
    rows = [{"x": 1}, {"x": 2}]
    assert sum_by_key(rows, "y") == 0.0
    
    # Только числовые значения
    rows = [{"val": 1}, {"val": 2.5}, {"val": -3}]
    assert sum_by_key(rows, "val") == 0.5   # 1 + 2.5 - 3 = 0.5
    
    # Игнорирование bool (True/False)
    rows = [{"n": 1}, {"n": True}, {"n": 2}, {"n": False}]
    assert sum_by_key(rows, "n") == 3.0     # True и False игнорируются
    
    # Проверка, что bool не суммируются, даже если численно равны 1/0
    assert sum_by_key([{"n": True}, {"n": False}], "n") == 0.0
    
    # Игнорирование нечисловых типов
    rows = [
        {"val": 10},
        {"val": "20"},        # строка
        {"val": [1,2]},       # список
        {"val": None},        # None
        {"val": {"a": 1}},    # dict
        {"val": 5.5}
    ]
    assert sum_by_key(rows, "val") == 15.5   # только 10 + 5.5
    
    # Отрицательные и большие числа
    rows = [{"a": -1e6}, {"a": 2e6}]
    assert sum_by_key(rows, "a") == 1e6
    
    # Ключ присутствует, но значение не числовое и не bool
    rows = [{"score": None}, {"score": "abc"}]
    assert sum_by_key(rows, "score") == 0.0
    
    # Смесь: числовые, bool, другие типы
    rows = [
        {"data": 5},
        {"data": True},
        {"data": 3.2},
        {"data": False},
        {"data": "ignore"},
        {"data": 0}
    ]
    assert sum_by_key(rows, "data") == 8.2   # 5 + 3.2 + 0 (True/False игнор)
    
    # Пустые словари в списке
    rows = [{}, {"val": 10}, {}, {"val": -2}]
    assert sum_by_key(rows, "val") == 8.0
    
    # Проверка, что walrus оператор не вызывает побочных эффектов вне условия
    rows = [{"x": 1}, {"x": 2}, {}]
    assert sum_by_key(rows, "x") == 3.0

# Запуск тестов (если модуль исполняется напрямую)
if __name__ == "__main__":
    test_update_item_fields()
    test_sum_by_key()
    print("All assertions passed.")