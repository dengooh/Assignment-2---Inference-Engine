from kb import KnowledgeBase
from tt import TruthTable
from bc import BackwardChaining

clauses = ["p2 => p3", "p3 => p1", "c => e", "b&e => f", "f&g => h", "p2&p1&p3 => d", "p1&p3 => c", "a", "b", "p2"]
kb = KnowledgeBase(clauses)
bc = BackwardChaining(kb)
result, proven = bc.query("d")
print("Backward Chaining result:", "YES:" + ', '.join(proven) if result else "NO")

tt = TruthTable(kb)
truth_table_result = tt.query("d")
print("Truth Table result:", truth_table_result)