from itertools import product


class TruthTable:
    def __init__(self, kb):

        """
        init of TT instance with KB

        :param:
            kb: the clauses
        """

        self.kb = kb

    def evaluate_clause(self, assignment, clause):

        """
        evaluate if an assignment satisfies a clause.

        :param:
            assignment: (tuple) a truth assignment for the symbols.
            clause: (str) the clause to evaluate.

        :return:
            True if the assignment satisfies the clause, False otherwise.
        """

        # create a dictionary of symbols and their assigned truth values.
        symbols = dict(zip(self.kb.symbols, assignment))

        # check if the clause is an implication.
        if "=>" in clause:
            # split the clause into premises (the conditions that need to be true for the conclusion to be considered
            # true) and conclusion (is the outcome or result that should be true if all the premises are true).
            premises, conclusion = map(str.strip, clause.split("=>"))
            # split the premises by '&' and strip any extra whitespace.
            premises = map(str.strip, premises.split("&"))

            # initialize a flag to check if all premises are satisfied.
            all_premises_satisfied = True

            # iterate over each premise in the premises list.
            for premise in premises:
                # check if the current premise is satisfied.
                if not symbols[premise]:
                    # if any premise is not satisfied, set the flag to False and break the loop.
                    all_premises_satisfied = False
                    break

            # check if the implication is satisfied based on the premises and conclusion.
            if not all_premises_satisfied or symbols[conclusion]:
                # if either all premises are not satisfied, or the conclusion is satisfied, return True.
                return True
            else:
                # if all premises are satisfied but the conclusion is not, return False.
                return False
        else:
            # evaluate the single symbol clause.
            return symbols[clause.strip()]

    def satisfies_clauses(self, assignment):

        """
        check if an assignment satisfies all clauses.

        :param:
            assignment: (tuple) a truth assignment for the symbols.

        :return:
            true if the assignment satisfies all clauses, False otherwise.
        """

        # initialize a flag to track if all clauses are satisfied.
        all_clauses_satisfied = True

        # iterate over each clause in the knowledge base.
        for clause in self.kb.clauses:
            # evaluate the current clause with the given assignment.
            clause_satisfied = self.evaluate_clause(assignment, clause)

            # if any clause is not satisfied, set the flag to False and break the loop.
            if not clause_satisfied:
                all_clauses_satisfied = False
                break

        # return whether all clauses are satisfied.
        return all_clauses_satisfied

    def query(self, proposition):

        """
        check if the given proposition is entailed by the knowledge base.

        :param:
            proposition: (str) proposition to query.

        :return:
            the number of models that satisfy the clauses and entail the proposition, or "NO" if the proposition is not a known symbol.
        """

        # ensure the proposition is among the known symbols
        if proposition not in self.kb.symbols:
            return "NO"

        # generate all possible truth assignments for the symbols.
        all_assignments = list(product([False, True], repeat=len(self.kb.symbols)))

        # initialize a list to store the satisfying models.
        satisfying_models = []

        # iterate over each assignment.
        for assignment in all_assignments:
            # check if the assignment satisfies all clauses.
            clauses_satisfied = self.satisfies_clauses(assignment)

            # check if the assignment entails the proposition.
            symbols_dict = dict(zip(self.kb.symbols, assignment))
            proposition_entails = symbols_dict[proposition]

            # if both conditions are met, add the assignment to the list of satisfying models.
            if clauses_satisfied and proposition_entails:
                satisfying_models.append(assignment)

        # return the number of satisfying models.
        return len(satisfying_models)
