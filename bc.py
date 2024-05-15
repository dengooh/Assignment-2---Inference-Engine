class BackwardChaining:
    def __init__(self, knowledge_base):
        """
        Initialize the BackwardChaining instance with a knowledge base containing facts and rules.
        """
        self.kb = knowledge_base

    def query(self, query):
        """
        Perform a backward chaining query to determine if the query can be derived from the knowledge base.

        :param query: The proposition symbol to be queried.
        :return: A tuple containing a boolean indicating if the query was proven and a list of all proven propositions.
        """
        proven = []
        result, _ = self._prove(query, proven, [])
        return result, proven

    def _prove(self, query, proven, in_process):
        """
        Recursive method to attempt to prove the query.

        :param query: The proposition to prove.
        :param proven: A list of already proven propositions to track the order of proof.
        :param in_process: A list to track propositions currently being processed to avoid cycles.
        :return: A tuple containing a boolean indicating if the query was proven and the list used for tracking recursion.
        """
        # Directly add and return if the query is a known fact or already proven
        if self.kb.is_fact(query):
            if query not in proven:
                proven.append(query)
            return True, proven

        # Avoid redundant processing and cycles
        if query in in_process:
            return False, in_process

        # Begin processing this query
        in_process.append(query)
        for rule in self.kb.get_rules_for(query):
            if all(self._prove(premise, proven, in_process)[0] for premise in rule):
                if query not in proven:
                    proven.append(query)  # Add to proven list when all premises are proven
                self.kb.add_fact(query)  # Optionally add to KB facts if that's needed
                in_process.remove(query)
                return True, proven

        in_process.remove(query)
        return False, in_process
