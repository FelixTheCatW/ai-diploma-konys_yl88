import unittest
import json
import os
import sys
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from json_utils import save_json, load_json, dict_to_json_text
from test_helpers import check

# Имя временного файла для тестов
TEST_FILE = "test_data.json"

test_data = {
    "models": [
        {"name": "Qwen2.5", "developer": "Alibaba"},
        {"name": "Midjourney v6", "developer": "Midjourney Inc"},
    ],
    "count": 2,
}

pprint(test_data)

class TestJsonUtils(unittest.TestCase):
    def setUp(self):
        """Очистка перед тестом."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def tearDown(self):
        """Удаление файла после теста."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_save_and_load_json(self):
        """Тест сохранения и загрузки JSON файла."""
        print("\n[ТЕСТ] save_json & load_json")

        save_json(TEST_FILE, test_data)
        print(f"  Файл '{TEST_FILE}' создан.")

        loaded = load_json(TEST_FILE)

        print(f"  Данные совпадают: {check(loaded == test_data)}")
        self.assertEqual(loaded, test_data)

        self.assertIn("models", loaded)

    def test_dict_to_json_text(self):
        """Тест преобразования словаря в JSON-строку."""
        print("\n[ТЕСТ] dict_to_json_text")

        simple_data = {"key": "значение", "num": 42}
        json_str = dict_to_json_text(simple_data)

        parsed = json.loads(json_str)
        print(f"  Строка валидна: {check(parsed == simple_data)}")
        self.assertEqual(parsed, simple_data)

        # Проверяем, что отступы есть (indent=4)
        has_indent = "\n    " in json_str
        print(f"  Отступы присутствуют: {check(has_indent)}")
        self.assertTrue(has_indent)

    def test_empty_data(self):
        """Тест с пустыми данными."""
        print("\n[ТЕСТ] Работа с пустыми данными")

        save_json(TEST_FILE, {})
        loaded = load_json(TEST_FILE)
        print(f"  Пустой объект {{}}: {check(loaded == {})}")
        self.assertEqual(loaded, {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
