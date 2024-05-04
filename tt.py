from itertools import product


class TruthTable:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def query(self, query):
        symbols = list(self.kb.symbols)
        models_count = 0
        total_models = 0  # Total models where the KB is true

        for combination in product([True, False], repeat=len(symbols)):
            assignment = dict(zip(symbols, combination))
            if self.evaluate_knowledge_base(assignment):
                total_models += 1
                if assignment.get(query, False):
                    models_count += 1

        # Check if the query is true in all models where the KB is true
        if models_count == total_models and total_models > 0:
            return f"YES: {models_count}"
        return "NO"

    def evaluate_knowledge_base(self, assignment):
        # Check each rule
        for conclusion, rules in self.kb.rules.items():
            conclusion_met = any(all(assignment.get(prem, False) for prem in premises) for premises in rules)
            if assignment.get(conclusion, False) != conclusion_met:
                return False

        # Ensure standalone facts are true
        for fact in self.kb.facts:
            if not assignment.get(fact, False):
                return False

        return True