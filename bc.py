class BackwardChaining:
    def __init__(self, knowledge_base):
        """
        initialize the BackwardChaining instance with a knowledge base (the knowledge base containing facts and rules).
        """
        self.kb = knowledge_base

    def query(self, query):
        """
        method to perform a backward chaining query

        :param query: str typed holding the proposition symbol required
        :return: a tuple containing a boolean indicating if the query was proven and the set of all proven propositions
        """

        # initialization of an empty set
        proven = set()
        # attempt to prove the query
        result, proven = self._prove(query, proven)
        # return the result and the proven propositions
        return result, proven

    def _prove(self, query, proven):
        """
        recursive method to attempt to prove the query
        :param query: (str) the proposition to prove
        :param proven: (set) a set of already proven propositions to avoid cycles
        :return: a tuple containing a boolean indicating if the query was proven and the updated set of proven
                propositions
        """

        # check if the query is already a known fact.
        if self.kb.is_fact(query):
            # add the query to the set of proven propositions
            proven.add(query)
            # return bool and the set
            return True, proven

        # necessary for redundant processing prevention
        if query in proven:
            # return false, query is being processed or unprovable
            return False, proven

        # add the processed query to the set
        proven.add(query)
        # get all rules concluding the query
        for rule in self.kb.get_rules_for(query):
            # recursively check if all premises of the rule can be proven
            if all(self._prove(premise, proven)[0] for premise in rule):
                # if proven, add the query as a fact to KB
                self.kb.add_fact(query)
                # and add to the set
                proven.add(query)
                # return true, query is proven
                return True, proven

        # remove the query from processing, as it's not proven
        proven.remove(query)
        # return false, indicating failure to prove the query
        return False, proven
