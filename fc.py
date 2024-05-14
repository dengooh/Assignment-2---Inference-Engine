class ForwardChaining:
    def __init__(self, knowledge_base):
        """
        Initialize the ForwardChaining instance with a knowledge base.

        Args:
            knowledge_base (KnowledgeBase): The knowledge base containing facts and rules.
        """
        self.kb = knowledge_base

    def query(self, query):
        """
        Perform a forward chaining query to determine if a specific proposition can be derived.

        Args:
            query (str): The proposition symbol to be queried.

        Returns:
            tuple: A tuple containing a boolean indicating if the query was derived,
                   and a set of all derived propositions during the process.
        """
        derived = set(self.kb.facts)  # Start with the known facts.
        added = True  # Flag to check if new facts were added in the iteration.

        while added:
            added = False  # Reset flag for each iteration.
            for conclusion, rules in self.kb.rules.items():
                for premises in rules:
                    # Check if all premises of the rule are in the derived set.
                    if all(premise in derived for premise in premises):
                        # Only add the conclusion if it's not already derived.
                        if conclusion not in derived:
                            derived.add(conclusion)
                            added = True
                            # If the conclusion is the query, return early.
                            if conclusion == query:
                                return True, derived

        # After processing all rules, check if the query has been derived.
        return query in derived, derived


