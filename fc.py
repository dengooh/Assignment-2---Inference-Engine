class ForwardChaining:
    def __init__(self, knowledge_base):

        """
        init of FC with KB

        :param:
            knowledge_base (KnowledgeBase): the clauses (horn form, and potentially general form)
        """

        self.kb = knowledge_base

    def query(self, query):

        """
        method to perform a forward chaining query to determine if a specific proposition can be derived.

        :param:
            query (string): The proposition symbol to be queried.
        :return:
            a tuple that contains a boolean to see if the proposition has been derived,
            and a list of all derived propositions during the process with the query last if derived.
        """

        derived = list(self.kb.facts)  # start with the known facts as a list.
        added = True  # flag to check if new facts were added in the iteration.
        query_found = False  # track if the query has been found

        while added:
            added = False  # reset flag for each iteration.
            for conclusion, rules in self.kb.rules.items():
                for premises in rules:
                    # initialize a flag to check if all premises are in the derived list.
                    all_premises_derived = True

                    # iterate over each premise in the current set of premises.
                    for premise in premises:
                        # check if the current premise is in the derived list.
                        if premise not in derived:
                            # if any premise is not in the derived list, set the flag to False and break the loop.
                            all_premises_derived = False
                            break

                    # check if all premises were found in the derived list.
                    if all_premises_derived:
                        # only add the conclusion if it's not already in the derived list, and it's not the query.
                        if conclusion not in derived and conclusion != query:
                            derived.append(conclusion)
                            added = True
                        # check if the conclusion is the query and mark it found but do not add yet.
                        if conclusion == query:
                            query_found = True

        # after processing all rules, if the query was found, append it last.
        if query_found:
            derived.append(query)

        # return whether the query was derived and the modified list of all derivations.
        return query_found, derived
