import os
import ast
from pathlib import Path


def get_module_docstring(filepath: Path) -> list[str]:
    """Извлекает модульную строку документации из файла .py с помощью AST."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        return ast.get_docstring(tree)
    except (SyntaxError, UnicodeDecodeError, OSError):
        return None


def get_functions_doc(filepath: Path) -> list[tuple[str, str]]:
    """
    Извлекает имена функций и их docstring из файла .py.
    Возвращает список кортежей (имя_функции, docstring).
    """
    functions = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node, True)
                functions.append(
                    (node.name, docstring if docstring else "👻 нет описания")
                )
    except (SyntaxError, UnicodeDecodeError, OSError):
        pass
    return functions


def scan_modules(directory: str) -> list[dict]:
    """
    Сканирует указанную директорию, собирает информацию о .py файлах.
    Возвращает список словарей с ключами: module_name, file_path, docstring, functions.
    """
    base_path = Path(directory).resolve()
    modules = []
    for py_file in base_path.glob("*_utils.py"):
        docstring = get_module_docstring(py_file)
        functions = get_functions_doc(py_file)
        modules.append(
            {
                "module_name": py_file.stem,
                "file_path": str(py_file),
                "docstring": docstring
                if docstring
                else "Мы не знаем, что это такое. Очень страшно.",
                "functions": functions,
            }
        )

    return modules



