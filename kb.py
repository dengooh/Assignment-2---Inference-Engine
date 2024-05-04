class KnowledgeBase:
    def __init__(self, clauses):
        self.facts = set()
        self.rules = {}
        self.symbols = set()
        self.parse_clauses(clauses)

    def parse_clauses(self, clauses):
        for clause in clauses:
            if "=>" in clause:
                premises, conclusion = map(str.strip, clause.split("=>"))
                premises = tuple(map(str.strip, premises.split("&")))
                self.symbols.update(premises)
                self.symbols.add(conclusion)
                if conclusion in self.rules:
                    self.rules[conclusion].append(premises)
                else:
                    self.rules[conclusion] = [premises]
            else:
                fact = clause.strip()
                self.facts.add(fact)
                self.symbols.add(fact)

    def add_fact(self, fact):
        self.facts.add(fact)

    def get_rules_for(self, conclusion):
        return self.rules.get(conclusion, [])

    def is_fact(self, proposition):
        return proposition in self.facts