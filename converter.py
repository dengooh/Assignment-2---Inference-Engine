import re


def convert_biconditionals(expression):
    """
    Convert biconditionals (<=>) to implications (=>).
    """
    pattern = re.compile(r'(\w+)\s*<=>\s*(\([\w\s=>~&|]+\)|\w+)')
    while pattern.search(expression):
        expression = pattern.sub(lambda m: f"({m.group(1)} => {m.group(2)}) & ({m.group(2)} => {m.group(1)})",
                                 expression)
    return expression


def convert_implications(expression):
    """
    Convert implications (=>) to disjunctions (~a | b).
    """
    pattern = re.compile(r'(\w+)\s*=>\s*(\([\w\s~&|]+\)|\w+)')
    while pattern.search(expression):
        expression = pattern.sub(lambda m: f"(~{m.group(1)} | {m.group(2)})", expression)
    return expression


def distribute_negations(expression):
    """
    Distribute negations over conjunctions and disjunctions.
    """
    expression = re.sub(r'~\(([\w\s~|]+)\s*&\s*([\w\s~|]+)\)', r'(~\1 | ~\2)', expression)
    expression = re.sub(r'~\(([\w\s~&]+)\s*\|\s*([\w\s~&]+)\)', r'(~\1 & ~\2)', expression)
    return expression


def normalize_disjunctions(expression):
    """
    Normalize disjunctions (||) to single disjunctions (|).
    """
    expression = re.sub(r'\|\|', '|', expression)
    return expression


def split_clauses(expression):
    """
    Split a normalized logical expression into individual clauses.
    """
    clauses = []
    for part in expression.split(';'):
        part = part.strip()
        if part:
            sub_clauses = part.split('&')
            for sub_clause in sub_clauses:
                sub_clause = sub_clause.strip()
                if sub_clause:
                    clauses.append(sub_clause)
    return clauses


def simplify_clause(clause):
    """
    Simplify a clause by converting disjunctions back to implications.
    """
    if '|' in clause:
        parts = clause.split('|')
        conclusion = parts[-1].strip()
        premises = [part.strip()[1:] for part in parts[:-1]]
        return f"{' & '.join(premises)} => {conclusion}"
    else:
        return clause


def convert_to_horn_clauses(expression):
    """
    Convert a general form logical expression to a list of Horn clauses.
    """
    # Step-by-step conversion
    expression = convert_biconditionals(expression)
    expression = convert_implications(expression)
    expression = distribute_negations(expression)
    expression = normalize_disjunctions(expression)

    # Split into clauses
    clauses = split_clauses(expression)

    # Simplify clauses
    simplified_clauses = [simplify_clause(clause) for clause in clauses]

    return simplified_clauses

