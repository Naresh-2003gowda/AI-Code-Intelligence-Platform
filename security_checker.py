import ast

def check_security(code):

    issues = []

    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):

                    if node.func.id == "eval":

                        issues.append(
                            "🚨 Critical: eval() can execute malicious code"
                        )

                    elif node.func.id == "exec":

                        issues.append(
                            "🚨 Critical: exec() can execute arbitrary code"
                        )

                    elif node.func.id == "input":

                        issues.append(
                            "⚠ User input detected. Validate input before use."
                        )

    except Exception as e:

        issues.append(
            f"Syntax Error: {e}"
        )

    return issues