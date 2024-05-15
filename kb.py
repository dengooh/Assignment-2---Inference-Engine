class KnowledgeBase:
    def __init__(self, clauses):
        """
        Initialize a new KnowledgeBase instance.

        :param clauses: (list): a list of strings representing the logical clauses,
                                which may be facts or rules (implications).
        """
        self.facts = []  # A list to store all known facts
        self.rules = {}  # A dictionary to store rules mapped from conclusions to premises
        self.symbols = []  # A list to store all unique symbols (propositions)
        self.parse_clauses(clauses)  # Parse the input clauses to populate facts, rules, and symbols

    def parse_clauses(self, clauses):
        """
        Void method to parse and store the input as facts or rules.

        :param clauses: (list): The list of strings provided during initialization.
        """
        for clause in clauses:
            if "=>" in clause:
                # If '=>' is in the clause, it's an implication rule.
                premises, conclusion = map(str.strip, clause.split("=>"))
                premises = tuple(map(str.strip, premises.split("&")))
                # Update the symbols list with premises and conclusion to ensure all are tracked.
                self.update_list(self.symbols, premises)
                self.update_list(self.symbols, [conclusion])
                # Append the premises to the conclusion key in the rules dictionary.
                if conclusion in self.rules:
                    if premises not in self.rules[conclusion]:
                        self.rules[conclusion].append(premises)
                else:
                    self.rules[conclusion] = [premises]
            else:
                # If no '=>' is found, it's a fact.
                fact = clause.strip()
                # Add the fact to the facts list if not already included.
                if fact not in self.facts:
                    self.facts.append(fact)
                # Also add the fact to the symbols list if not already included.
                if fact not in self.symbols:
                    self.symbols.append(fact)

    def add_fact(self, fact):
        """
        A void method to add a new fact to the knowledge base.

        :param fact: (str) The fact to add.
        """
        if fact not in self.facts:
            self.facts.append(fact)

    def get_rules_for(self, conclusion):
        """
        Retrieve the rules that conclude with a specific proposition.

        :param conclusion: (str) The conclusion for which to get the premises.

        :return: A list of tuples, each tuple representing a set of premises.
        """
        return self.rules.get(conclusion, [])

    def is_fact(self, proposition):
        """
        Check if a given proposition is a known fact.

        :param proposition: (str) The proposition to check.

        :return: True if the proposition is a known fact, False otherwise.
        """
        return proposition in self.facts

    def update_list(self, target_list, items):
        """
        A utility method to add items to a list without adding duplicates.

        :param target_list: (list) The list to update.
        :param items: (iterable) Items to add to the list.
        """
        for item in items:
            if item not in target_list:
                target_list.append(item)
