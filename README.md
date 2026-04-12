# AI Diploma Project
 
## Как запустить (локально в VS Code)
1) Установите Python 3.10+
2) (Рекомендуется) создайте окружение и установите зависимости:
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate
   # macOS/Linux: source venv/bin/activate
   pip install -r requirements.txt
   ```
   git checkout -b feature/m1-project-structure
3) Запуск CLI:
   ```bash
   python -m src.cli
   ```
 
## Структура
- `src/core.py` — логика (items, validate, stats)
- `src/parsers.py` — парсинг/нормализация
- `src/storage.py` — JSON, состояние, экспорт/импорт
- `src/cli.py` — запуск и команды
- `colab/` — ноутбуки lesson_XX / hw_XX
- `data/` — локальные данные (в проде лучше БД/volume)