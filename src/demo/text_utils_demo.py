import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from text_utils import normalize_text, word_count, contains_word
from test_helpers import check


class TestTextUtils(unittest.TestCase):
    def test_normalize_text(self):
        """Тест нормализации текста."""
        print("\n[ТЕСТ] normalize_text")

        res = normalize_text("  Привет   Мир  ")
        print(f"  Лишние пробелы и регистр: '{res}' -> {check(res == 'привет мир')}")
        self.assertEqual(res, "привет мир")

        res_empty = normalize_text("   ")
        print(f"  Пустая строка: '{res_empty}' -> {check(res_empty == '')}")
        self.assertEqual(res_empty, "")

    def test_word_count(self):
        """Тест подсчета количества слов."""
        print("\n[ТЕСТ] word_count")

        count = word_count("Раз два три четыре")
        print(f"  Обычный текст (4 слова): {count} -> {check(count == 4)}")
        self.assertEqual(count, 4)

        count_empty = word_count("")
        print(f"  Пустая строка: {count_empty} -> {check(count_empty == 0)}")
        self.assertEqual(count_empty, 0)

    def test_contains_word(self):
        """Тест поиска целого слова."""
        print("\n[ТЕСТ] contains_word")

        src_text = "Мама мыла раму"
        # Поиск существующего слова
        res_found = contains_word(src_text, "раму")
        print(
            f"  Слово 'раму' найдено в '{src_text}': {res_found} -> {check(res_found)}"
        )
        self.assertTrue(res_found)

        # Поиск несуществующего (подстрока)
        res_sub = contains_word("скобка", "коб")
        print(f"  Подстрока 'коб' в 'скобка': {res_sub} -> {check(not res_sub)}")
        self.assertFalse(res_sub)


if __name__ == "__main__":
    unittest.main(verbosity=2)
import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from text_utils import normalize_text, word_count, contains_word
from test_helpers import check

class TestTextUtils(unittest.TestCase):

    def test_normalize_text(self):
        """Тест нормализации текста."""
        print("\n[ТЕСТ] normalize_text")
        
        res = normalize_text("  Привет   Мир  ")
        print(f"  Лишние пробелы и регистр: '{res}' -> {check(res == 'привет мир')}")
        self.assertEqual(res, "привет мир")

        res_empty = normalize_text("   ")
        print(f"  Пустая строка: '{res_empty}' -> {check(res_empty == '')}")
        self.assertEqual(res_empty, "")

    def test_word_count(self):
        """Тест подсчета количества слов."""
        print("\n[ТЕСТ] word_count")

        count = word_count("Раз два три четыре")
        print(f"  Обычный текст (4 слова): {count} -> {check(count == 4)}")
        self.assertEqual(count, 4)

        count_empty = word_count("")
        print(f"  Пустая строка: {count_empty} -> {check(count_empty == 0)}")
        self.assertEqual(count_empty, 0)

    def test_contains_word(self):
        """Тест поиска целого слова."""
        print("\n[ТЕСТ] contains_word")

        src_text = "Мама мыла раму"
        # Поиск существующего слова
        res_found = contains_word(src_text, "раму")
        print(f"  Слово 'раму' найдено в '{src_text}': {res_found} -> {check(res_found)}")
        self.assertTrue(res_found)

        # Поиск несуществующего (подстрока)
        res_sub = contains_word("скобка", "коб")
        print(f"  Подстрока 'коб' в 'скобка': {res_sub} -> {check(not res_sub)}")
        self.assertFalse(res_sub)

if __name__ == "__main__":    
    unittest.main(verbosity=2)