class KnowledgeBase:
    def __init__(self, clauses):
        """
        initialize a new KnowledgeBase instance

        :param clauses: (list): a list of strings representing the logical clauses,
                                which may be facts or rules (implications).
        """
        # a set to store all known facts
        self.facts = set()
        # a dictionary to store rules mapped from conclusions to premises
        self.rules = {}
        # a set to store all unique symbols (propositions)
        self.symbols = set()
        # parse the input clauses to populate facts, rules, and symbols
        self.parse_clauses(clauses)

    def parse_clauses(self, clauses):
        """
        void method to parse and store the input as facts or rules

        :param clauses: (list): list of strings provided during init
        """

        for clause in clauses:
            if "=>" in clause:
                # if '=>' is in the clause, it's an implication rule
                premises, conclusion = map(str.strip, clause.split("=>"))
                print(premises)
                premises = tuple(map(str.strip, premises.split("&")))
                # update the symbols set with premises and conclusion to ensure all are tracked
                self.symbols.update(premises)
                self.symbols.add(conclusion)
                # append the premises to the conclusion key in the rules dictionary
                if conclusion in self.rules:
                    self.rules[conclusion].append(premises)
                else:
                    self.rules[conclusion] = [premises]
            else:
                # if no '=>' is found, it's a fact
                fact = clause.strip()
                # add the fact to the facts set
                self.facts.add(fact)
                # also addd the fact to the symbols set
                self.symbols.add(fact)

    def add_fact(self, fact):
        """
        a void method to add a new fact to the knowledge base

        :param fact: (str) te fact to add
        """
        self.facts.add(fact)

    def get_rules_for(self, conclusion):
        """
        retrieve the rules that conclude with a specific proposition

        :param conclusion: (str) the conclusion for which to get the premises

        :return: a list of tuples, each tuple representing a set of premises
        """

        # return the premises associated with the conclusion
        return self.rules.get(conclusion, [])

    def is_fact(self, proposition):
        """
        check if a given proposition if a known fact

        :param proposition: (str) the proposition to check

        :return: true if the proposition is a known fact, false otherwise
        """

        # return true if the proposition is in the facts set
        return proposition in self.facts