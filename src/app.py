import curses
from user_menu import scan_modules
from text_utils import wrap_text


def draw_interface(
    stdscr,
    modules: list[dict],
    current_idx: int,
    show_functions: bool,
    functions_for_idx: int,
):

    stdscr.clear()
    height, width = stdscr.getmaxyx()
    delimiter = "=" * width

    curses.use_default_colors()
    for i in range(0, 255):
        curses.init_pair(i + 1, i, -1)

    # footer
    help_msg = "↑/↓: выбор модуля | Enter: показать функции | q: выход"
    stdscr.addstr(height - 1, 0, help_msg[: width - 1], curses.color_pair(48))

    cur_y = 0
    stdscr.addstr(cur_y, 0, "Меню".center(width))
    cur_y += 1
    stdscr.addstr(cur_y, 0, ("*" * 12).center(width))
    cur_y += 1
    # Меню
    for i, mod in enumerate(modules):
        name = mod["module_name"]

        if i == current_idx:
            stdscr.addstr(cur_y, 0, f"👉 {name}".center(width))
        else:
            stdscr.addstr(cur_y, 0, f"    {name}".center(width))
        cur_y += 1
    
    cur_y = len(modules) + 1

    cur_y += 1
    stdscr.addstr(cur_y, 0, delimiter, curses.color_pair(244))
    cur_y += 1
    doc_start_y = cur_y
    stdscr.addstr(cur_y, 0, "Описание модуля:", curses.color_pair(192))
    doc_text = modules[current_idx]["docstring"]

    for line in wrap_text(doc_text, width - 4):
        stdscr.addstr(cur_y + 1, 2, line)
        cur_y += 1

    funcs = modules[functions_for_idx]["functions"]
    cur_y += 2
    if funcs:
        # Заголовок
        stdscr.addstr(cur_y, 0, "Функции модуля:", curses.A_BOLD)
        cur_y += 1

        for fname, fdoc in funcs:
            stdscr.addstr(cur_y, 2, f"📌 {fname}")
            cur_y += 1

            for line in wrap_text(fdoc, width - 6):
                stdscr.addstr(cur_y, 4, line, curses.color_pair(250))
                cur_y += 1

            cur_y += 1
    else:
        stdscr.addstr(cur_y, 2, "👻 Функции не найдены")

    stdscr.refresh()


def main_curses(stdscr, directory: str):
    curses.curs_set(0)
    stdscr.nodelay(False)
    stdscr.keypad(True)

    modules = scan_modules(directory)
    if not modules:
        stdscr.addstr(
            0,
            0,
            "Нет модулей .py в указанной директории. Нажмите любую клавишу для выхода.",
        )
        stdscr.getch()
        return

    current_idx = 0
    show_functions = True
    functions_for_idx = current_idx

    while True:
        draw_interface(stdscr, modules, current_idx, show_functions, functions_for_idx)
        key = stdscr.getch()

        if key == ord("q") or key == ord("Q"):
            break
        elif key == curses.KEY_UP:
            current_idx = (current_idx - 1) % len(modules)
            functions_for_idx = current_idx
        elif key == curses.KEY_DOWN:
            current_idx = (current_idx + 1) % len(modules)
            functions_for_idx = current_idx
        elif key == ord("\n") or key == curses.KEY_ENTER:
            pass


def run(target_dir):
    curses.wrapper(main_curses, target_dir)
