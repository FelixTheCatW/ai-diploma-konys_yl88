# Определяем цвета
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"  # сброс цвета

from pprint import pprint
from data_utils import *

ai_models = [
    {
        "name": "GPT-4",
        "developer": "OpenAI",
        "year": 2023,
        "fact": "Может сдать экзамены на адвоката (бар) в США, попав в 90-й процентиль"
    },
    {
        "name": "GPT-3.5",
        "developer": "OpenAI",
        "year": 2022,
        "fact": "Самая популярная версия ChatGPT до выхода GPT-4"
    },
    {
        "name": "GPT-4o",
        "developer": "OpenAI",
        "year": 2024,
        "fact": "Мультимодальная модель, работает с текстом, звуком и изображениями в реальном времени"
    },
    {
        "name": "BERT",
        "developer": "Google",
        "year": 2018,
        "fact": "Его название расшифровывается как Bidirectional Encoder Representations from Transformers"
    },
    {
        "name": "DALL-E 2",
        "developer": "OpenAI",
        "year": 2022,
        "fact": "Умеет редактировать изображения по текстовому описанию (inpainting)"
    },
    {
        "name": "Claude 3",
        "developer": "Anthropic",
        "year": 2024,
        "fact": "Разработан с особым акцентом на безопасность и 'конституционное' поведение"
    },
    {
        "name": "YandexGPT",
        "developer": "Яндекс",
        "year": 2024,
        "fact": "Поддерживает диалоговые сценарии на русском языке с учётом региональных особенностей"
    },
    {
        "name": "DeepSeek",
        "developer": "DeepSeek (High-Flyer)",
        "year": 2024,
        "fact": "Открытая модель с архитектурой MoE, известная крайне низкой стоимостью обучения"
    },
    {
        "name": "Qwen",
        "developer": "Alibaba Cloud",
        "year": 2024,
        "fact": "Многоязычная модель, лидирует в бенчмарках китайского и английского языков"
    }
]


qwen = find_by_name(ai_models, "Qwen")
print(f"{GREEN}Найдена модель:{RESET}")
pprint(qwen, indent=2, width=80)

dob_24 = filter_by_value(ai_models, "year", 2024)
print(f"{GREEN}Модели 2024 года выпуска:{RESET}")
pprint(dob_24, width=80, indent=2)

total_models = count_items(ai_models)
total_dob_24 = count_items(dob_24)
print("Всего моделей:", total_models)
print("Моделей 2024 года выпуска:", total_dob_24)