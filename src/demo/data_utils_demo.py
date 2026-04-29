import unittest
import os
import sys
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data_utils import find_by_name, filter_by_value, count_items
from test_helpers import check

ai_models = [
    {"name": "GPT-4", "developer": "OpenAI", "type": "LLM"},
    {"name": "Claude 3", "developer": "Anthropic", "type": "LLM"},
    {"name": "Mistral Large", "developer": "Mistral AI", "type": "LLM"},
    {"name": "Midjourney v6", "developer": "Midjourney Inc", "type": "ImageGen"},
    {"name": "Qwen2.5", "developer": "Alibaba", "type": "LLM"},
]

pprint(ai_models)

class TestAIModels(unittest.TestCase):
    def test_find_by_name(self):
        """Поиск модели по имени."""
        print("\n[ТЕСТ] find_by_name (Поиск по имени)")

        # Успешный поиск
        res = find_by_name(ai_models, "Qwen2.5")
        dev = res["developer"] if res else None
        print(f"  Найти 'Qwen2.5': Разработчик={dev} -> {check(dev == 'Alibaba')}")
        self.assertIsNotNone(res)
        self.assertEqual(res["developer"], "Alibaba")

        # Поиск несуществующего
        res = find_by_name(ai_models, "Gemini Ultra")
        print(f"  Найти 'Gemini': {res} -> {check(res is None)}")
        self.assertIsNone(res)

    def test_filter_by_value(self):
        """Фильтрация моделей по типу или разработчику."""
        print("\n[ТЕСТ] filter_by_value (Фильтрация)")

        # Фильтр: Только LLM
        llms = filter_by_value(ai_models, "type", "LLM")
        names = [m["name"] for m in llms]
        print(
            f"  Тип 'LLM': найдено {len(llms)} шт. -> {check(len(llms) == 4 and 'GPT-4' in names)}"
        )
        self.assertEqual(len(llms), 4)
        self.assertIn("GPT-4", names)

        # Фильтр: Разработчик Mistral AI
        mistral_models = filter_by_value(ai_models, "developer", "Mistral AI")
        names_m = [m["name"] for m in mistral_models]
        print(
            f"  Разработчик 'Mistral AI': {names_m} -> {check(len(mistral_models) == 1)}"
        )
        self.assertEqual(len(mistral_models), 1)
        self.assertEqual(mistral_models[0]["name"], "Mistral Large")

    def test_count_items(self):
        """Подсчет количества моделей."""
        print("\n[ТЕСТ] count_items (Подсчет)")

        total = count_items(ai_models)
        print(f"  Всего моделей: {total} -> {check(total == 5)}")
        self.assertEqual(total, 5)

        empty = count_items([])
        print(f"  Пустой список: {empty} -> {check(empty == 0)}")
        self.assertEqual(empty, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
