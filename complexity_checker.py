import ast

def analyze_complexity(code):

    score = 100

    functions = 0
    loops = 0
    conditions = 0

    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                functions += 1

            elif isinstance(node, (ast.For, ast.While)):

                loops += 1
                score -= 5

            elif isinstance(node, ast.If):

                conditions += 1
                score -= 3

        score = max(score, 0)

        return {
            "score": score,
            "functions": functions,
            "loops": loops,
            "conditions": conditions
        }

    except Exception:

        return {
            "score": 0,
            "functions": 0,
            "loops": 0,
            "conditions": 0
        }