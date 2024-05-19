class BackwardChaining:
    def __init__(self, knowledge_base):

        """
        init BC instance with KB
        """

        self.kb = knowledge_base

    def query(self, query):

        """
        perform a query to see if the proposition can be derived

        :param:
            query: proposition symbol to be queried.
        :return:
            tuple containing a boolean indicating if the query was proven and a list of all proven propositions.
        """

        proven = []
        result, proven_propositions = self.prove(query, proven, [])
        return result, proven_propositions

    def prove(self, query, proven, in_process):

        """
        recursive method to attempt to prove the query.

        :param:
            query (string): the proposition to prove.
            proven (list): list of already proven propositions to track the order of proof.
            in_process (list): a list to track propositions currently being processed to avoid cycles.
        :return:
            a tuple containing a boolean indicating if the query was proven and the list used for tracking recursion.
        """

        # add and return if the query is a known fact or already proven
        if self.kb.is_fact(query):
            if query not in proven:
                proven.append(query)
            return True, proven

        # avoid redundant processing and cycles
        if query in in_process:
            return False, in_process

        # begin processing this query
        in_process.append(query)

        # get all rules that can lead to the query
        rules = self.kb.get_rules_for(query)
        if not rules:
            # if no rules can derive the query, it cannot be proven
            in_process.remove(query)
            return False, in_process

        # iterate through all rules that can lead to the query
        for rule in rules:
            # initialize a flag to check if all premises of the rule are proven
            all_premises_proven = True

            # check premise in the rule
            for premise in rule:
                # recursively attempt to prove each premise
                premise_proven, _ = self.prove(premise, proven, in_process)

                # if any premise is not proven, set the flag to False and break the loop
                if not premise_proven:
                    all_premises_proven = False
                    break

            # if all premises are proven, the query is proven
            if all_premises_proven:
                if query not in proven:
                    # add to proven list when all premises are proven
                    proven.append(query)
                in_process.remove(query)
                return True, proven

        # remove the query from in_process as it is no longer being processed
        in_process.remove(query)

        # return False indicating the query was not proven and the current state of in_process
        return False, in_process