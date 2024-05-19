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
        result= self.prove(query, proven, [])
        return result, proven

    def prove(self, query, proven, in_process):
        """
        Recursive method to attempt to prove the query.

        :param query: The proposition to prove.
        :type query: str
        :param proven: A list of already proven propositions to track the order of proof.
        :type proven: list
        :param in_process: A list to track propositions currently being processed to avoid cycles.
        :type in_process: list
        :return: A tuple containing a boolean indicating if the query was proven and the list used for tracking recursion.
        :rtype: tuple
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

        # Iterate through all rules that can lead to the query
        for rule in self.kb.get_rules_for(query):
            # Initialize a flag to check if all premises of the rule are proven
            all_premises_proven = True

            # Check each premise in the rule
            for premise in rule:
                # Recursively attempt to prove each premise
                premise_proven, _ = self.prove(premise, proven, in_process)

                # If any premise is not proven, set the flag to False and break the loop
                if not premise_proven:
                    all_premises_proven = False
                    break

            # If all premises are proven, the query is proven
            if all_premises_proven:
                if query not in proven:
                    proven.append(query)  # Add to proven list when all premises are proven
                self.kb.add_fact(query)  # Optionally add to KB facts if that's needed
                in_process.remove(query)
                return True, proven

        # Remove the query from in_process as it is no longer being processed
        in_process.remove(query)

        # Return False indicating the query was not proven and the current state of in_process
        return False, in_process
