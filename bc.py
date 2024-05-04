class BackwardChaining:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def query(self, query):
        proven = set()
        result, proven = self._prove(query, proven)
        return result, proven

    def _prove(self, query, proven):
        if self.kb.is_fact(query):
            proven.add(query)
            return True, proven

        if query in proven:
            return False, proven

        proven.add(query)
        for rule in self.kb.get_rules_for(query):
            if all(self._prove(premise, proven)[0] for premise in rule):
                self.kb.add_fact(query)
                proven.add(query)
                return True, proven
        proven.remove(query)
        return False, proven