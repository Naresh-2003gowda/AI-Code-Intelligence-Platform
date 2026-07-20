import ast

def get_refactoring_suggestions(code):

    suggestions = []

    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                if ast.get_docstring(node) is None:

                    suggestions.append(
                        f"Add a docstring to function '{node.name}'"
                    )

                if len(node.args.args) > 3:

                    suggestions.append(
                        f"Function '{node.name}' has many parameters. Consider refactoring."
                    )

        if "try:" not in code:

            suggestions.append(
                "Consider adding exception handling using try-except blocks."
            )

        if ":" in code and "->" not in code:

            suggestions.append(
                "Consider adding type hints for better maintainability."
            )

    except Exception as e:

        suggestions.append(str(e))

    return suggestions