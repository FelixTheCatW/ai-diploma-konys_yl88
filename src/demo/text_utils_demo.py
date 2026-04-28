import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from text_utils import normalize_text, word_count, contains_word


class TestTextUtils(unittest.TestCase):
    def test_normalize_text_basic(self):        
        print("\n--- ТЕСТ: normalize_text (Базовый) ---")
        input_str = "  Привет   Мир  "
        print(f"Входная строка: '{input_str}'")

        result = normalize_text(input_str)
        print(f"Результат нормализации: '{result}'")

        self.assertEqual(result, "привет мир")
        print("УСПЕХ: Строка приведена к нижнему регистру, лишние пробелы удалены.")

    def test_word_count_normal(self):
        """Тест подсчета слов в обычном предложении."""
        print("\n--- ТЕСТ: word_count (Обычный текст) ---")
        text = "Раз два три четыре"
        print(f"Текст: '{text}'")

        count = word_count(text)
        print(f"Количество слов: {count}")

        self.assertEqual(count, 4)
        print("УСПЕХ: Количество слов посчитано верно.")

    def test_contains_word_true(self):
        """Тест поиска слова, которое есть в тексте."""
        print("\n--- ТЕСТ: contains_word (Слово найдено) ---")
        text = "Мама мыла раму"
        word = "раму"
        print(f"Текст: '{text}', Ищем слово: '{word}'")

        result = contains_word(text, word)
        print(f"Результат поиска: {result}")

        self.assertTrue(result)
        print("УСПЕХ: Слово 'раму' найдено в тексте.")

    def test_contains_word_false_substring(self):
        """Тест, что поиск идет по целым словам, а не подстрокам."""
        print("\n--- ТЕСТ: contains_word (Ложное совпадение подстроки) ---")
        text2 = "скобка"
        word2 = "коб"  # подстрока есть, но слова нет

        print(f"Текст: '{text2}', Ищем слово: '{word2}'")

        result = contains_word(text2, word2)
        print(f"Результат поиска: {result}")

        self.assertFalse(result)
        print("УСПЕХ: Подстрока не считается отдельным словом.")

if __name__ == "__main__":
    # Запуск тестов с выводом комментариев
    unittest.main(verbosity=2)
