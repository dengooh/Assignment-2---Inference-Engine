from itertools import product


class TruthTable:
    def __init__(self, knowledge_base):
        """
        initialize the TruthTable instance with knowledge base

        :param knowledge_base: the knowledge base containing facts and rules
        """
        self.kb = knowledge_base

    def query(self, query):
        """
        public method to perform a truth table query to determine if the knowledge base entails the query

        :param query: (str) the proposition symbol to be queried

        :return: (str) "YES: (number of models that entail the query)", or "NO" if no entailment
        """

        # list of all unique proposition symbols in the KB
        symbols = list(self.kb.symbols)
        # count of models where the query is true
        models_count = 0
        # total count of models where the KB is true
        total_models = 0

        # generate all possible truth assignments for the symbols.
        for combination in product([True, False], repeat=len(symbols)):
            # create a dictionary from symbols to their truth values (truth table)
            assignment = dict(zip(symbols, combination))
            # evaluate the entire knowledge base under the current truth assignment
            if self.evaluate_knowledge_base(assignment):
                # increment total models where the KB is true
                total_models += 1
                # check if the query is also true in this model
                if assignment.get(query, False):
                    # increment the count by 1
                    models_count += 1
        # check if the query is true in all models where the KB is true
        if models_count == total_models and total_models > 0:
            # return "YES" and the number of models
            return f"YES: {models_count}"
        # if no entailment(s) then return "NO"
        return "NO"

    def evaluate_knowledge_base(self, assignment):
        """
        evaluate the truth of the entire knowledge base under a given truth assignment.

        :param assignment: (dict) a dictionary mapping each symbol to a truth value (True or False).

        :return: true if the knowledge base is true under this assignment, false otherwise
        """
        # check each rule defined in the KB
        for conclusion, rules in self.kb.rules.items():
            # check if any set of premises that leads to the conclusion is true
            conclusion_met = any(all(assignment.get(prem, False) for prem in premises) for premises in rules)
            # the conclusion must match the logical outcome of the premises
            if assignment.get(conclusion, False) != conclusion_met:
                # if not, the KB isn't true under this assignment
                return False

        # ensure that all standalone facts are true in the current assignment.
        for fact in self.kb.facts:
            if not assignment.get(fact, False):
                # if any fact is not true, the KB isn't true under this assignment
                return False

        # if all checks pass, the KB is true under this assignment
        return True