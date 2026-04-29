import curses
import winsound
from user_menu import scan_modules, run_module_file
from text_utils import wrap_text

colors_init: set = set()


class ScreenWriter:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.y = 0
        self.x = 0

    def new_line(self):
        self.y += 1

    def write(self, text: str, indent: int, color: int):
        try:
            if self.y >= self.height - 1:
                return False

            if not text or not text.strip():
                return True

            if len(text) > self.width - self.x - 1 - indent:
                text = text[: self.width - 1 - indent]

            if color > 0 and color not in colors_init:
                curses.init_pair(color + 1, color, -1)

            self.stdscr.addstr(self.y, self.x + indent, text, curses.color_pair(color))
            self.y += 1

            return True
        except curses.error:
            return False

    def write_wrapped(self, text, indent=0, color=0):
        lines = wrap_text(text, self.width - indent - 2)
        for line in lines:
            return self.write(line, indent, color)

        return True

    def write_separator(self, char="=", color=0):
        separator = char * (self.width - 2)
        self.write(separator, 0, color)
        self.y += 1
        return True


def draw_interface(
    stdscr,
    modules: list[dict],
    current_idx: int,
    show_demo: bool,
):
    stdscr.clear()

    curses.use_default_colors()
    for i in range(0, 255):
        try:
            curses.init_pair(i + 1, i, -1)
        except curses.error:
            pass

    height, width = stdscr.getmaxyx()

    sw = ScreenWriter(stdscr)

    names_max_lens = max((len(x["module_name"]) for x in modules), default=10) * 2
    sw.write("Меню".center(width), 0, 48)
    sw.write(("~" * names_max_lens).center(width), 0, 48)

    for i, mod in enumerate(modules):
        name = mod["module_name"]
        if i == current_idx:
            line = f"👉 {name}".center(width - 2)
        else:
            line = f"    {name}".center(width - 2)
        sw.write(line, 0, 81)

    sw.write_separator("=", 244)

    if show_demo:
        demo_path = modules[current_idx]["demo"]
        if demo_path:
            demo_result = run_module_file(demo_path)

            if demo_result["stdout"]:
                sw.write("Сообщения выполнения тестов:", 0, 203)
                original_lines = demo_result["stdout"].splitlines()
                for line in original_lines:
                    if not sw.write_wrapped(line, 2):
                        break

            if demo_result["stderr"]:
                sw.new_line()
                sw.write("Вывод результатов фреймворка unittest:", 0, 203)
                error_lines = demo_result["stderr"].splitlines()
                for line in error_lines:
                    if line:  # Пропускаем совсем пустые, если нужно
                        if not sw.write_wrapped(line, 2):
                            break
    else:
        sw.write("Описание модуля:", 0, 13)
        doc_text = modules[current_idx]["docstring"]
        sw.write_wrapped(doc_text, 2)

        funcs = modules[current_idx]["functions"]
        if funcs:
            sw.write("Функции модуля:", 0, 34)

            for func_name, func_doc in funcs:
                sw.write(f"  📌 {func_name}", 0, 0)

                if func_doc:
                    for line in func_doc.splitlines():
                        sw.write_wrapped(line, 4, 250)

                sw.new_line()

    # --- Footer (подвал) ---
    help_msg = "↑/↓: выбор модуля | Enter: запустить тесты | q: выход"
    stdscr.addstr(height - 1, 0, help_msg, curses.color_pair(48))

    stdscr.refresh()


def main_curses(stdscr, directory: str):
    curses.curs_set(0)
    stdscr.nodelay(False)
    stdscr.keypad(True)

    modules = scan_modules(directory)
    if not modules:
        stdscr.addstr(0, 0, "Нет модулей. Нажмите любую клавишу.")
        stdscr.getch()
        return

    current_idx = 0
    show_demo = False

    while True:
        draw_interface(stdscr, modules, current_idx, show_demo)
        key = stdscr.getch()

        if key == ord("q") or key == ord("Q"):
            break
        elif key == curses.KEY_UP:
            current_idx = (current_idx - 1) % len(modules)
            winsound.Beep(200, 100)
            show_demo = False
        elif key == curses.KEY_DOWN:
            current_idx = (current_idx + 1) % len(modules)
            winsound.Beep(200, 100)
            show_demo = False
        elif key == ord("\n") or key == curses.KEY_ENTER:
            winsound.Beep(160, 400)
            show_demo = True


def run(target_dir):
    curses.wrapper(main_curses, target_dir)
