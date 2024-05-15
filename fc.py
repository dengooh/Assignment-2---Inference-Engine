class ForwardChaining:
    def __init__(self, knowledge_base):
        """
        Initialize the ForwardChaining instance with a knowledge base.

        :param knowledge_base (KnowledgeBase): The knowledge base containing facts and rules.
        """
        self.kb = knowledge_base

    def query(self, query):
        """
        Perform a forward chaining query to determine if a specific proposition can be derived.

        :param query (str): The proposition symbol to be queried.

        :return: A tuple containing a boolean indicating if the query was derived,
                 and a list of all derived propositions during the process with the query last if derived.
        """
        derived = list(self.kb.facts)  # Start with the known facts as a list.
        added = True  # Flag to check if new facts were added in the iteration.
        query_found = False  # Track if the query has been found

        while added:
            added = False  # Reset flag for each iteration.
            for conclusion, rules in self.kb.rules.items():
                for premises in rules:
                    # Check if all premises of the rule are in the derived list.
                    if all(premise in derived for premise in premises):
                        # Only add the conclusion if it's not already in the derived list and it's not the query.
                        if conclusion not in derived and conclusion != query:
                            derived.append(conclusion)
                            added = True
                        # Check if the conclusion is the query and mark it found but do not add yet.
                        if conclusion == query:
                            query_found = True

        # After processing all rules, if the query was found, append it last.
        if query_found:
            derived.append(query)

        # Return whether the query was derived and the modified list of all derivations.
        return query_found, derived
