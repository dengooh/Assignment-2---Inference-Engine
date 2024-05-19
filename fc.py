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

        :param query: The proposition symbol to be queried.
        :type query: str
        :return: A tuple containing a boolean indicating if the query was derived,
                 and a list of all derived propositions during the process with the query last if derived.
        :rtype: tuple
        """
        derived = list(self.kb.facts)  # Start with the known facts as a list.
        added = True  # Flag to check if new facts were added in the iteration.
        query_found = False  # Track if the query has been found

        while added:
            added = False  # Reset flag for each iteration.
            for conclusion, rules in self.kb.rules.items():
                for premises in rules:
                    # Initialize a flag to check if all premises are in the derived list.
                    all_premises_derived = True

                    # Iterate over each premise in the current set of premises.
                    for premise in premises:
                        # Check if the current premise is in the derived list.
                        if premise not in derived:
                            # If any premise is not in the derived list, set the flag to False and break the loop.
                            all_premises_derived = False
                            break

                    # Check if all premises were found in the derived list.
                    if all_premises_derived:
                        # Only add the conclusion if it's not already in the derived list, and it's not the query.
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
