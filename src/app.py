import curses
from user_menu import scan_modules, run_module_file
from text_utils import wrap_text


class ScreenWriter:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.y = 0
        self.x = 0

    def move_to(self, y, x):
        self.y = y
        self.x = x

    def write(self, text="", color=0):
        if self.y >= self.height - 1:
            return False

        try:
            if not text:
                self.y += 1
                return True
            if not text:
                self.y += 1
                return True
            safe_text = text[: self.width - self.x - 1]
            self.stdscr.addstr(self.y, self.x, safe_text, color)
            self.y += 1
            return True
        except curses.error:
            return False

    def write_wrapped(self, text, indent=0, color=0):
        if self.y >= self.height - 1:
            return False

        lines = wrap_text(text, self.width - indent - 2)
        for line in lines:
            if not self.write(" " * indent + line, color):
                return False
        return True

    def write_separator(self, char="=", color=0):
        if self.y >= self.height - 1:
            return False
        separator = char * self.width
        try:
            self.stdscr.addstr(self.y, 0, separator, color)
            self.y += 1
            return True
        except curses.error:
            return False


def draw_interface(
    stdscr,
    modules: list[dict],
    current_idx: int,
    show_demo: bool,
):
    stdscr.clear()

    # Инициализация цветов
    curses.use_default_colors()
    for i in range(0, 255):
        try:
            curses.init_pair(i + 1, i, -1)
        except curses.error:
            pass

    height, width = stdscr.getmaxyx()

    # Создаем помощника для вывода
    sw = ScreenWriter(stdscr)

    names_max_lens = max((len(x["module_name"]) for x in modules), default=10) * 2
    sw.write("Меню".center(width))
    sw.write(("*" * names_max_lens).center(width))

    for i, mod in enumerate(modules):
        name = mod["module_name"]
        if i == current_idx:
            line = f"👉 {name}".center(width)
        else:
            line = f"    {name}".center(width)
        sw.write(line)
        
    sw.write_separator("=", curses.color_pair(244))

    if show_demo:
        demo_path = modules[current_idx]["demo"]
        if demo_path:
            demo_result = run_module_file(demo_path)

            if demo_result["stdout"]:
                sw.write("Сообщения выполнения тестов:", color=curses.color_pair(203))                
                original_lines = demo_result["stdout"].splitlines()
                for line in original_lines:
                    # Используем write_wrapped для автоматического переноса
                    if not sw.write_wrapped(line, indent=2):
                        break

            if demo_result["stderr"]:
                sw.write()
                if sw.y < height - 1:
                    sw.write(
                        "Вывод результатов фреймворка unittest:", curses.color_pair(203)
                    )
                    error_lines = demo_result["stderr"].splitlines()
                    for line in error_lines:
                        if line:  # Пропускаем совсем пустые, если нужно
                            if not sw.write_wrapped(
                                line, indent=2
                            ):
                                break
    else:
        sw.write("Описание модуля:", curses.color_pair(13))
        doc_text = modules[current_idx]["docstring"]
        sw.write_wrapped(doc_text, indent=2)

        funcs = modules[current_idx]["functions"]
        if funcs:
            sw.write("Функции модуля:", curses.color_pair(34))

            for fname, fdoc in funcs:
                sw.write(f"  📌 {fname}")

                if fdoc:
                    for line in fdoc.splitlines():
                        if line.strip():
                            if not sw.write_wrapped(
                                line, indent=4, color=curses.color_pair(250)
                            ):
                                break
                sw.write()

    # --- Footer (подвал) ---
    help_msg = "↑/↓: выбор модуля | Enter: показать функции | q: выход"
    try:
        stdscr.addstr(height - 1, 0, help_msg[: width - 1], curses.color_pair(48))
    except curses.error:
        pass

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
            show_demo = False
        elif key == curses.KEY_DOWN:
            current_idx = (current_idx + 1) % len(modules)
            show_demo = False
        elif key == ord("\n") or key == curses.KEY_ENTER:
            show_demo = True


def run(target_dir):
    curses.wrapper(main_curses, target_dir)
