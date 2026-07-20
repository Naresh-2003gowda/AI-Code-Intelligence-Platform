import ast

def generate_summary(code):

    functions = 0
    classes = 0
    imports = 0

    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                functions += 1

            elif isinstance(node, ast.ClassDef):
                classes += 1

            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                imports += 1

        return {
            "functions": functions,
            "classes": classes,
            "imports": imports
        }

    except:

        return {
            "functions": 0,
            "classes": 0,
            "imports": 0
        }