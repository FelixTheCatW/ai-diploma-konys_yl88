import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data_utils import find_by_name, filter_by_value, count_items

# Тестовые данные: AI Модели
ai_models = [
    {"name": "GPT-4", "developer": "OpenAI", "type": "LLM"},
    {"name": "Claude 3", "developer": "Anthropic", "type": "LLM"},
    {"name": "Mistral Large", "developer": "Mistral AI", "type": "LLM"},
    {"name": "Midjourney v6", "developer": "Midjourney Inc", "type": "ImageGen"},
    {"name": "Qwen2.5", "developer": "Alibaba", "type": "LLM"},
]


class TestAIModels(unittest.TestCase):
    def test_find_by_name(self):
        """Поиск модели по имени."""
        print("\n[TEST] find_by_name (AI Models)")

        # Ищем Qwen
        res = find_by_name(ai_models, "Qwen2.5")
        dev = res["developer"] if res else None
        print(
            f"  Find 'Qwen2.5': Developer={dev} -> {'OK' if dev == 'Alibaba' else 'FAIL'}"
        )
        self.assertIsNotNone(res)
        self.assertEqual(res["developer"], "Alibaba")

        # Ищем несуществующую
        res = find_by_name(ai_models, "Gemini Ultra")
        print(f"  Find 'Gemini': {res} -> {'OK' if res is None else 'FAIL'}")
        self.assertIsNone(res)

    def test_filter_by_value(self):
        """Фильтрация моделей по типу или разработчику."""
        print("\n[TEST] filter_by_value")

        # Фильтр: Только LLM
        llms = filter_by_value(ai_models, "type", "LLM")
        names = [m["name"] for m in llms]
        print(f"  Type 'LLM': {len(llms)} models -> {names}")
        self.assertEqual(len(llms), 4)
        self.assertIn("GPT-4", names)

        # Фильтр: Разработчик Mistral AI
        mistral_models = filter_by_value(ai_models, "developer", "Mistral AI")
        print(f"  Dev 'Mistral AI': {[m['name'] for m in mistral_models]}")
        self.assertEqual(len(mistral_models), 1)
        self.assertEqual(mistral_models[0]["name"], "Mistral Large")

    def test_count_items(self):
        """Подсчет количества моделей."""
        print("\n[TEST] count_items")

        total = count_items(ai_models)
        print(f"  Total models: {total} -> {'OK' if total == 5 else 'FAIL'}")
        self.assertEqual(total, 5)

        empty = count_items([])
        print(f"  Empty list: {empty} -> {'OK' if empty == 0 else 'FAIL'}")
        self.assertEqual(empty, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
