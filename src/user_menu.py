import sys
from text_utils import normalize_text
from data_utils import count_items


def show_menu():
    print("Выберите действие:")
    print("1 - обработать текст")
    print("2 - посчитать количество объектов")
    print("0 - выход")


def run_choice(choice):
    if choice == "1":
        print(normalize_text(f"   {sys.version}   "))
    elif choice == "2":
        print(count_items(sys.modules.keys()))
    elif choice == "0":
        print("Программа завершена")
    else:
        print("Неизвестная команда")
