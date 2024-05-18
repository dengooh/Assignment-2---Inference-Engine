from itertools import product


class TruthTable:
    def __init__(self, knowledge_base):
        """
        Initialize a new TruthTable instance.

        :param knowledge_base: (KnowledgeBase): An instance of KnowledgeBase containing the clauses.
        """
        self.kb = knowledge_base

    def evaluate_clause(self, assignment, clause):
        """
        Evaluate if an assignment satisfies a clause.

        :param assignment: (tuple) A truth assignment for the symbols.
        :param clause: (str) The clause to evaluate.

        :return: True if the assignment satisfies the clause, False otherwise.
        """
        symbols = dict(zip(self.kb.symbols, assignment))
        if "=>" in clause:
            premises, conclusion = map(str.strip, clause.split("=>"))
            premises = map(str.strip, premises.split("&"))
            return not all(symbols[p] for p in premises) or symbols[conclusion]
        else:
            return symbols[clause.strip()]

    def satisfies_clauses(self, assignment):
        """
        Check if an assignment satisfies all clauses.

        :param assignment: (tuple) A truth assignment for the symbols.

        :return: True if the assignment satisfies all clauses, False otherwise.
        """
        return all(self.evaluate_clause(assignment, clause) for clause in self.kb.clauses)

    def query(self, proposition):
        """
        Check if the given proposition is entailed by the knowledge base.

        :param proposition: (str) The proposition to query.

        :return: The number of models that satisfy the clauses and entail the proposition.
        """
        all_assignments = list(product([False, True], repeat=len(self.kb.symbols)))
        satisfying_models = [
            assignment for assignment in all_assignments
            if self.satisfies_clauses(assignment) and dict(zip(self.kb.symbols, assignment))[proposition]
        ]
        return len(satisfying_models)

