import curses
from user_menu import scan_modules, run_module_file
from text_utils import wrap_text
from file_utils import save_text


def draw_interface(
    stdscr,
    modules: list[dict],
    current_idx: int,
    show_demo: bool,
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

    names_max_lens = max(map(lambda x: len(x["module_name"]), modules)) + 4
    cur_y = 0
    stdscr.addstr(cur_y, 0, "Меню".center(width))
    cur_y += 1
    stdscr.addstr(cur_y, 0, ("*" * names_max_lens).center(width))
    cur_y += 1

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

    if show_demo:
        demo_path = modules[current_idx]["demo"]
        if demo_path:
            demo_result = run_module_file(demo_path)
            if demo_result["stdout"]:
                original_lines = demo_result["stdout"].splitlines()
                
                for line in original_lines:                    
                    wrapped_lines = wrap_text(line, width - 4)
                   
                    for sub_line in wrapped_lines:
                        if cur_y < height:
                            stdscr.addstr(cur_y, 2, sub_line)
                            cur_y += 1
                        else:
                            break
            
            if demo_result["stderr"]:
                cur_y += 1  
                stdscr.addstr(cur_y, 2, "Вывод результатов фреймворка unittest:", curses.color_pair(203))
                cur_y += 1                
                error_lines = demo_result["stderr"].splitlines()
                for line in error_lines:
                    if not line:
                        stdscr.addstr(cur_y, 2, "", curses.color_pair(203))
                        cur_y += 1
                        continue
                        
                    wrapped_errors = wrap_text(line, width - 4)
                    for sub_line in wrapped_errors:
                        if cur_y + 1 < height:
                            stdscr.addstr(cur_y, 2, sub_line, curses.color_pair(203))
                            cur_y += 1
                        else:
                            break

    else:
        cur_y += 1
        stdscr.addstr(cur_y, 0, "Описание модуля:", curses.color_pair(34))
        cur_y += 1
        doc_text = modules[current_idx]["docstring"]
        for line in wrap_text(doc_text, width - 4):
            stdscr.addstr(cur_y, 2, line)
            cur_y += 1

        funcs = modules[current_idx]["functions"]

        if funcs:
            # Заголовок
            stdscr.addstr(cur_y, 0, "Функции модуля:", curses.color_pair(34))
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
        stdscr.addstr(0, 0, "Нет модулей. Нажмите любую клавишу.")
        stdscr.getch()
        return

    current_idx = 0
    show_functions = True
    show_demo = False
    functions_for_idx = current_idx

    while True:
        draw_interface(stdscr, modules, current_idx, show_demo)
        key = stdscr.getch()
        show_demo = False
        if key == ord("q") or key == ord("Q"):
            break
        elif key == curses.KEY_UP:
            current_idx = (current_idx - 1) % len(modules)
            functions_for_idx = current_idx
        elif key == curses.KEY_DOWN:
            current_idx = (current_idx + 1) % len(modules)
            functions_for_idx = current_idx
        elif key == ord("\n") or key == curses.KEY_ENTER:
            show_demo = True


def run(target_dir):
    curses.wrapper(main_curses, target_dir)
