def get_imports_in_current_file(file):
    import inspect
    import ast

    current_file = inspect.getfile(file if file else lambda: None)

    with open(current_file, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                imports.append(alias.name)
    return imports
