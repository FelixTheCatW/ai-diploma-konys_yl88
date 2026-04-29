import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from file_utils import save_text, load_text, append_text, count_lines
from test_helpers import check

# Имя временного файла для тестов
TEST_FILE = "test_temp.txt"


class TestFileUtils(unittest.TestCase):
    def setUp(self):
        """Очистка перед каждым тестом, если файл остался."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def tearDown(self):
        """Удаление временного файла после теста."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_save_and_load(self):
        """Тест сохранения и загрузки текста."""
        print("\n[ТЕСТ] save_text & load_text")

        content = "Привет, мир!\nЭто тест."
        save_text(TEST_FILE, content)
        print(f"  Сохранено: '{content}'")

        loaded = load_text(TEST_FILE)
        print(f"  Загружено: '{loaded}' -> {check(loaded == content)}")
        self.assertEqual(loaded, content)

    def test_append_text(self):
        """Тест добавления текста в конец файла."""
        print("\n[ТЕСТ] append_text")

        save_text(TEST_FILE, "Строка 1")
        append_text(TEST_FILE, "Строка 2")

        result = load_text(TEST_FILE)
        expected = "Строка 1\nСтрока 2"

        print(f"  Результат: {repr(result)} -> {check(result == expected)}")
        self.assertEqual(result, expected)

    def test_count_lines(self):
        """Тест подсчета количества строк."""
        print("\n[ТЕСТ] count_lines")

        save_text(TEST_FILE, "Раз\nДва\nТри")
        count = count_lines(TEST_FILE)

        print(f"  Строк в файле: {count} -> {check(count == 3)}")
        self.assertEqual(count, 3)

        save_text(TEST_FILE, "")
        count_empty = count_lines(TEST_FILE)
        print(f"  Строк в пустом: {count_empty} -> {check(count_empty == 0)}")
        self.assertEqual(count_empty, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
