import unittest
import os
import sys
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from csv_utils import save_csv, load_csv, count_csv_rows, sum_column
from test_helpers import check

# Имя временного файла
TEST_FILE = "test_data.csv"

# Тестовые данные: Фрукты и цены
test_rows = [
    ["Товар", "Кол-во", "Цена"],
    ["Яблоко", "10", "50"],
    ["Груша", "5", "80"],
    ["Банан", "20", "30"],
]

pprint(test_rows)

class TestCsvUtils(unittest.TestCase):
    def setUp(self):
        """Очистка перед тестом."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def tearDown(self):
        """Удаление файла после теста."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_save_and_load_csv(self):
        """Тест сохранения и загрузки CSV."""
        print("\n[ТЕСТ] save_csv & load_csv")

        save_csv(TEST_FILE, test_rows)
        print(f"  Файл '{TEST_FILE}' создан.")

        loaded = load_csv(TEST_FILE)
        print(f"  Данные совпадают -> {check(loaded == test_rows)}")
        self.assertEqual(loaded, test_rows)

    def test_count_csv_rows(self):
        """Тест подсчета количества строк."""
        print("\n[ТЕСТ] count_csv_rows")

        save_csv(TEST_FILE, test_rows)
        count = count_csv_rows(TEST_FILE)

        # 1 заголовок + 3 строки данных = 4
        print(f"  Всего строк: {count} (ожид. 4) -> {check(count == 4)}")
        self.assertEqual(count, 4)

    def test_sum_column(self):
        """Тест суммирования числового столбца."""
        print("\n[ТЕСТ] sum_column")

        save_csv(TEST_FILE, test_rows)

        # Суммируем столбец "Цена" (индекс 2)
        # 50 + 80 + 30 = 160
        total = sum_column(TEST_FILE, 2, has_header=True)

        print(f"  Сумма цен: {total} (ожид. 160) -> {check(total == 160)}")
        self.assertEqual(total, 160)

        # Суммируем столбец "Кол-во" (индекс 1)
        # 10 + 5 + 20 = 35
        total_qty = sum_column(TEST_FILE, 1, has_header=True)
        print(f"  Сумма кол-ва: {total_qty} (ожид. 35) -> {check(total_qty == 35)}")
        self.assertEqual(total_qty, 35)


if __name__ == "__main__":
    unittest.main(verbosity=2)
