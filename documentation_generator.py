import ast

def generate_docs(code):

    docs = []

    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                function_name = node.name

                parameters = [
                    arg.arg for arg in node.args.args
                ]

                doc_template = f'''
Function: {function_name}

Suggested Documentation:

"""
Description:
Explain what {function_name} does.

Parameters:
{", ".join(parameters)}

Returns:
Specify return value.
"""
'''

                docs.append(doc_template)

    except Exception as e:

        docs.append(f"Error: {e}")

    return docs
