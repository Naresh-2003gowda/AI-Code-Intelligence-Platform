import ast

def detect_bugs(code):

    bugs = []

    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                if ast.get_docstring(node) is None:

                    bugs.append(
                        f"⚠ Function '{node.name}' has no docstring"
                    )

            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):

                    if node.func.id == "eval":

                        bugs.append(
                            "🚨 Security Risk: eval() detected"
                        )

    except Exception as e:

        bugs.append(
            f"❌ Syntax Error: {e}"
        )

    return bugs